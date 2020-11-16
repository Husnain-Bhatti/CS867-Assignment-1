{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def rgbExclusion(image, channel):\n",
    "    red_img = np.array(np.zeros(image.shape), dtype='i')\n",
    "    green_img = np.array(np.zeros(image.shape), dtype='i')\n",
    "    blue_img = np.array(np.zeros(image.shape), dtype='i')\n",
    "    red_channel = image[:,:,0]\n",
    "    green_channel = image[:,:,1]\n",
    "    blue_channel = image[:,:,2]\n",
    "    red_img[:,:,0] = red_channel\n",
    "    green_img[:,:,1] = green_channel\n",
    "    blue_img[:,:,2] = blue_channel\n",
    "    excluded_img = image.copy()\n",
    "    if (channel == 'red'):\n",
    "        excluded_img[:,:,0] = np.zeros([image.shape[0], image.shape[1]])\n",
    "    elif (channel == 'green'):\n",
    "        excluded_img[:,:,1] = np.zeros([image.shape[0], image.shape[1]])\n",
    "    elif (channel == 'blue'):\n",
    "        excluded_img[:,:,2] = np.zeros([image.shape[0], image.shape[1]])\n",
    "    return  red_img, green_img, blue_img, excluded_img"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
