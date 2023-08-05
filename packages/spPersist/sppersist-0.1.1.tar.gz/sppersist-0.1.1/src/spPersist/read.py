import wget, tarfile, zipfile, os, shutil, requests
from zipfile import ZipFile
import scanpy as sc
import pandas as pd
import anndata



def visium(gex: str, pos: str):
  '''
  visium takes cell by gene count file name gex and tissue position lists pos, 
  and return an annotated data object with spatial coordinates.
  Note that gex and pos should be formatted as Spance Ranger outputs.
  '''
  ad = sc.read_10x_h5(gex)
  coords = pd.read_csv(pos,index_col=0)
  coords.columns = ["in_tissue", "array_row", "array_col", "pxl_col_in_fullres", "pxl_row_in_fullres"]
  ad.obs = pd.merge(ad.obs, coords, how="left", left_index=True, right_index=True)
  ad.obsm['spatial'] = ad.obs[["pxl_row_in_fullres", "pxl_col_in_fullres"]].values
  ad.obs.drop(columns=["pxl_row_in_fullres", "pxl_col_in_fullres"], inplace=True)
  return ad

def merfish(gex: str, pos: str):
  '''
  merfish takes cell by gene count file name gex and
  metadata file pos that contains spatial coordinates, 
  and return an annotated data object with spatial coordinates.
  Note that gex and pos should be formatted as Vizgen outputs.
  '''
  adata = anndata.AnnData(pd.read_csv(gex, header=0, index_col=0))
  

  # fmt: off
  coords = pd.read_csv(pos, header=0, index_col=0)
  coords.columns = ["fov", "volume", "center_x", "center_y", "min_x", "max_x", "min_y", "max_y"]
  # fmt: on

  adata.obs = pd.merge(adata.obs, coords, how="left", left_index=True, right_index=True)
  adata.obsm['spatial'] = adata.obs[["center_x", "center_y"]].values
  adata.obs.drop(columns=["center_x", "center_y"], inplace=True)
  return adata


def zenodo_urls_from_doi(doi: str):
  '''
  zenodo_urls_from_doi takes a zenodo doi number doi and
  returns a list of urls of the files in the repository.
  '''

  record_id = doi.split('.')[-1]

  # get request (do not need to provide access token since public
  r = requests.get(f"https://zenodo.org/api/records/{record_id}")  # params={'access_token': ACCESS_TOKEN})
  return [f['links']['self'] for f in r.json()['files']]


def zenodo_to_h5(doi: str, filename: str, ttype: str):
  '''
  zenodo_to_h5 takes a zenodo doi number doi that 
  contains a tar or zip file named filename and ttype specifying
  if the technology type is Visium or MERFISH, and
  exports a zip file of annotated objects from 
  the Visium or MERFISH samples in the dataset as h5 files.
  '''

  urls = zenodo_urls_from_doi(doi)
  for url in urls:
    if filename in url:
      path = '/'.join(url.split('/')[:-1]) + '/'
  
  if path is None:
    raise NameError('The repository does not contain a file named filename.')

  url_to_h5(path,filename=filename,ttype=ttype)


def accession_to_h5(gse: str, filename: str, ttype: str):
  '''
  accession_to_h5 takes a GEO accession number gse that 
  contains a tar or zip file named filename and ttype specifying
  if the technology type is Visium or MERFISH, and
  exports a zip file of annotated objects from 
  the Visium or MERFISH samples in the dataset as h5 files.
  '''

  path = 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE'+gse[3:6]+'nnn/'+gse+'/suppl/'
  url_to_h5(path, filename=filename, ttype=ttype)


def url_to_h5(path: str, filename: str, ttype: str):
  '''
  url_to_h5 takes a url path that contains a 
  tar or zip file named filename and ttype specifying
  if the technology type is Visium or MERFISH, and
  exports a zip file of annotated objects from 
  the Visium or MERFISH samples in the dataset as h5 files.
  '''

  url = path + filename
  if filename not in os.listdir():
    wget.download(url, bar=wget.bar_adaptive)

  if tarfile.is_tarfile(filename):
    repository = tarfile.open(filename) 
    filenames = repository.getnames()
  elif zipfile.is_tarfile(filename):
    repository = ZipFile(filename)
    filenames = repository.namelist()
  else:
    raise ValueError('filename is not tar or zip file.')

  if ttype == 'Visium':
    samplelist = list(filter(lambda s: s.endswith('.h5'), filenames))
  elif ttype == 'MERFISH':
    samplelist = list(filter(lambda s: 'cell_by_gene' in s, filenames))
  else:
    raise ValueError('ttype is not either Visium or MERFISH.')

  sampleids = [s.split('_')[0] for s in samplelist]
  
  # helper function for extracting a sample
  def extractsample(members, sampleid):
    for member in members:
      if member.isfile():
        fname = member.name
      else:
        fname = member

      if sampleid in fname:
        yield member

  # helper function for emptying a given directory
  def emptydir(folder):
    for filename in os.listdir(folder):
      file_path = os.path.join(folder, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              os.unlink(file_path)
          elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))


  data_path = './data/'
  h5_path = './h5/'

  if not os.path.exists(data_path):
    os.mkdir(data_path)
  if not os.path.exists(h5_path):
    os.mkdir(h5_path)

  emptydir(h5_path)

  for sampleid in sampleids:
    emptydir(data_path)
    
    # extract files for a given sample id to the visium foler
    repository.extractall(path=data_path,
                   members=extractsample(repository, sampleid))

    for filename in os.listdir(data_path):
      if ttype == 'Visium':
        if filename.endswith('.h5'):
          gex = data_path + filename
        if 'positions' in filename:
          pos = data_path + filename
      elif ttype == 'MERFISH':
        if 'cell_by_gene' in filename:
          gex = data_path + filename
        if 'cell_metadata' in filename:
          pos = data_path + filename
      else:
        raise ValueError('ttype is not either Visium or MERFISH.')
    
    if gex is None or pos is None:
      raise NameError('The repository does not contain Visium or Vizgen formatted files.')
    
    if gex.endswith('.h5'):
      adata = visium(gex, pos)
    else:
      adata = merfish(gex, pos)

    savefilename = sampleid + '.h5'
    adata.write_h5ad(h5_path+savefilename)
  
  # zip h5 files
  shutil.make_archive('h5', 'zip', h5_path)