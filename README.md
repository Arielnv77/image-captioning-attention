🌁 ## Image Captioning with Visual Attention

(or: why the model sees “a man in a red” everywhere)

📌 Project overview

This project explores Image Captioning, a task that combines Computer Vision and Natural Language Processing to generate textual descriptions from images.

The goal of the project is not to achieve state-of-the-art results, but to:
	•	build a complete and functional pipeline
	•	understand how visual and textual components interact
	•	analyze why and how the model fails under realistic constraints

The final model works… but often poorly — and that is precisely the most interesting part of the project.

🧠 Motivation

Image Captioning looks deceptively simple:

“Just look at the image and describe it.”

In practice, it is a highly data-dependent and fragile task.
This project was designed to experience those limitations first-hand by training a model under deliberately constrained conditions:
	•	small dataset
	•	short training
	•	frozen visual encoder
	•	simple recurrent decoder


🧩 Architecture

The model follows a classic Encoder–Decoder with Attention architecture:

🔹 Encoder (Vision)
	•	Pretrained ResNet (ImageNet)
	•	Used as a feature extractor
	•	Outputs a spatial feature map (visual regions)
	•	Encoder weights are frozen

🔹 Attention mechanism
	•	Computes attention weights over visual regions
	•	Allows the decoder to focus on different parts of the image at each time step

🔹 Decoder (Language)
	•	LSTM-based decoder
	•	Generates the caption word by word
	•	Uses teacher forcing during training


📂 Dataset
	•	Based on Flickr8k
	•	A small subset (~800 images) was intentionally used
	•	Each image has multiple human-written captions
	•	This choice highlights:
	•	dataset bias
	•	mode collapse in generation
	•	limitations of language modeling with few examples


⚙️ Training setup
	•	Framework: PyTorch
	•	Loss: Cross-Entropy (padding ignored)
	•	Optimizer: Adam
	•	Training epochs: 3
	•	Hardware: CPU only

Training loss evolution:
        Epoch 1 → Loss: 5.75
        Epoch 2 → Loss: 4.91
        Epoch 3 → Loss: 4.57


Results (honest version)

The model is able to generate captions for unseen images, but the quality is often:
	•	repetitive
	•	overly generic
	•	biased towards frequent patterns

A common example:

Image without people → “a man in a man in a red”

This behavior is not a bug — it is a textbook example of mode collapse caused by:
	•	small dataset size
	•	strong caption frequency bias
	•	limited language modeling capacity


Error analysis (the important part)

Key factors behind the poor captions:
	•	Dataset size: far too small for a generative task
	•	Dataset bias: over-representation of people and common phrases
	•	Frozen encoder: visual features cannot adapt to the task
	•	Simple decoder: limited linguistic expressiveness
	•	Short training: insufficient exposure to diverse patterns

When the model is uncertain, it defaults to the most probable sentence fragments it has seen during training.

This project clearly demonstrates how data limitations dominate architectural choices in generative models.


🎯 Conclusions

This project shows that:
	•	Image Captioning is significantly harder than it appears
	•	A correct architecture does not guarantee good results
	•	Data quantity and balance are critical
	•	Poor results can still provide strong learning value

Understanding why a model fails is often more valuable than obtaining a superficially good output.
