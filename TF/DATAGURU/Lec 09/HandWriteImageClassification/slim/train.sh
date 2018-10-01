cd /Users/zoe/Documents/GitHub/July-NLP/TF/DATAGURU/Lec\ 09/HandWriteImageClassification/slim
python train_image_classifier.py \
--train_dir model=\
--dataset_name myimages=\
--dataset_split_name=train \
--dataset_dir=images \
--batch_size=10 \
--max_number_of_steps=10000 \
--model_name=inception_v3 
pause