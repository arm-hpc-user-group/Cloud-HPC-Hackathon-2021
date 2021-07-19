import os

FOLDER = 'output/aws/c6gn/builtin'

for folder in os.listdir(FOLDER):
    with open(os.path.join(FOLDER, folder, f'rfm_{folder}_job.out')) as f:
        [ info, _, nodes, _, mpi, _, omp ] = folder.split('___')
        omp = omp.replace('_', '')
        compiler = info.split('__')[-1]
        try:
            teps = f.readlines()[25]
            teps = teps.split(' ')[-1][:-1]
            print(compiler, nodes, mpi, omp, teps, sep='\t')
        except:
            pass
