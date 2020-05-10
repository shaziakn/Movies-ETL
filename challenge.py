{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(f'wikipedia.movies.json', mode='r') as file:\n",
    "    wiki_movies_raw = json.load(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/envs/PythonData/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3063: DtypeWarning: Columns (10) have mixed types.Specify dtype option on import or set low_memory=False.\n",
      "  interactivity=interactivity, compiler=compiler, result=result)\n"
     ]
    }
   ],
   "source": [
    "kaggle_metadata = pd.read_csv(f'the_movies_dataset/movies_metadata.csv')\n",
    "ratings = pd.read_csv(f'the_movies_dataset/ratings.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies_df = pd.DataFrame(wiki_movies_raw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_movie(movie):\n",
    "    movie = dict(movie) #create a non-destructive copy\n",
    "    alt_titles = {}\n",
    "    for key in ['Also known as','Arabic','Cantonese','Chinese','French',\n",
    "                'Hangul','Hebrew','Hepburn','Japanese','Literally',\n",
    "                'Mandarin','McCune–Reischauer','Original title','Polish',\n",
    "                'Revised Romanization','Romanized','Russian',\n",
    "                'Simplified','Traditional','Yiddish']:\n",
    "        if key in movie:\n",
    "            alt_titles[key] = movie[key]\n",
    "            movie.pop(key)\n",
    "    if len(alt_titles) > 0:\n",
    "        movie['alt_titles'] = alt_titles\n",
    "\n",
    "    return movie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies = [movie for movie in wiki_movies_raw\n",
    "               if ('Director' in movie or 'Directed by' in movie)\n",
    "                   and 'imdb_link' in movie\n",
    "                   and 'No. of episodes' not in movie]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "clean_movies = [clean_movie(movie) for movie in wiki_movies]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "wiki_movies_df = pd.DataFrame(clean_movies)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
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
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
