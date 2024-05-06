import os
import shutil
import random

def split_dataset(data_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    for category in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category)

        for split in ['train', 'val', 'test']:
            split_path = os.path.join(category_path, split)
            os.makedirs(split_path, exist_ok=True)

        # Get all image files in this category
        image_files = [f for f in os.listdir(category_path) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg') or f.lower().endswith('.png')]
        random.shuffle(image_files)

        # Calculate splits based on ratios
        num_images = len(image_files)
        train_split_idx = int(train_ratio * num_images)
        val_split_idx = train_split_idx + int(val_ratio * num_images)

        # Move images to respective destination folders
        for i, image_file in enumerate(image_files):
            src_path = os.path.join(category_path, image_file)
            if i < train_split_idx:
                dst_path = os.path.join(category_path, 'train', image_file)
            elif i < val_split_idx:
                dst_path = os.path.join(category_path, 'val', image_file)
            else:
                dst_path = os.path.join(category_path, 'test', image_file)
            shutil.move(src_path, dst_path)

data_dir = "C:\\Users\\Zehir\\Documents\\GitHub\\plant-health-analyzer\\data\\diseased\\"
split_dataset(data_dir)
