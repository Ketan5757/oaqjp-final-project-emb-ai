from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="Your Name",
    description="A package for detecting emotions from text using Watson or Hugging Face models.",
)
