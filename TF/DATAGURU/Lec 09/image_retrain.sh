cd /Users/zoe/Documents/GitHub/July-NLP/TF/DATAGURU/Lec\ 09
# export MODE='Zoe'
python retrain.py \
--bottleneck_dir bottleneck \
--how_many_training_steps 200 \
--model_dir ../Lec\ 08/inception_model \
--output_graph output_graph.pb \
--output_labels output_labels.txt \
--image_dir retrain/data/train \
pause