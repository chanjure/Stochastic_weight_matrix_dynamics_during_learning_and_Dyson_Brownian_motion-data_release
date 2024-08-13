jupyter nbconvert --to notebook --execute scripts/SRBM-scaling_analysis.ipynb
mv scripts/SRBM-scaling_analysis.nbconvert.ipynb scripts/SRBM-scaling_analysis.ipynb
nbstripout scripts/SRBM-scaling_analysis.ipynb

jupyter nbconvert --to notebook --execute scripts/TSmodel-scaling_analysis.ipynb
mv scripts/TSmodel-scaling_analysis.nbconvert.ipynb scripts/TSmodel-scaling_analysis.ipynb
nbstripout scripts/TSmodel-scaling_analysis.ipynb

rm -rf ./images/*

python -m pytest -v --cov-config=.coveragerc --cov=./ test/
rm -rf ./models/*
