import wget, tarfile, os, shutil
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

def accession_to_h5(gse: str):
  '''
  accession_to_h5 takes GEO Accession number 
  gse that contains a raw tar file of samples 
  of Spance Ranger outputs, and
  exports a zip file of annotated objects from 
  the Visium samples in the dataset as h5 files.
  '''

  filename = gse+'_RAW.tar'
  url = 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE'+gse[3:6]+'nnn/'+gse+'/suppl/'+ filename
  if filename not in os.listdir():
    wget.download(url, bar=wget.bar_adaptive)

  tar = tarfile.open(filename)
  sampleids = [s.split('_')[0] for s in list(filter(lambda s: s.endswith('.h5'), tar.getnames()))]
  
  # helper function for extracting a sample
  def extractsample(members, sampleid):
    for tarinfo in members:
      if sampleid in tarinfo.name:
        yield tarinfo

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

  if 'data/' not in os.listdir():
    os.mkdir(data_path)
  if 'h5/' not in os.listdir():
    os.mkdir(h5_path)

  emptydir(h5_path)

  for sampleid in sampleids:
    emptydir(data_path)
    
    # extract files for a given sample id to the visium foler
    tar.extractall(path=data_path,
                   members=extractsample(tar, sampleid))

    for filename in os.listdir(data_path):
      # Visium files
      if filename.endswith('.h5'):
        gex = data_path + filename
      if 'positions' in filename:
        pos = data_path + filename
      # MERFISH files
      if 'cell_by_gene' in filename:
        gex = data_path + filename
      if 'cell_metadata' in filename:
        pos = data_path + filename
    
    if gex.endswith('.h5'):
      adata = visium(gex, pos)
    else:
      adata = merfish(gex, pos)

    savefilename = sampleid + '.h5'
    adata.write_h5ad(h5_path+savefilename)
  
  # zip h5 files
  shutil.make_archive(gse+'_h5', 'zip', h5_path)