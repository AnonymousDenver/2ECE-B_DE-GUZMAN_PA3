{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d07f4125-4308-4160-95cf-806995e8a6d1",
   "metadata": {},
   "source": [
    "# PROBLEM 2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "4ba2bc65-0677-44c3-9dfc-046050c7cd8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd # To access pandas liblary "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "06ca6b0f-bfa0-43df-afe4-981d4e193908",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First five rows with odd-numbered columns:\n",
      "               Model  cyl   hp     wt  vs  gear\n",
      "0          Mazda RX4    6  110  2.620   0     4\n",
      "1      Mazda RX4 Wag    6  110  2.875   0     4\n",
      "2         Datsun 710    4   93  2.320   1     4\n",
      "3     Hornet 4 Drive    6  110  3.215   1     3\n",
      "4  Hornet Sportabout    8  175  3.440   0     3\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# PART (a)\n",
    "\n",
    "cars = pd.read_csv('cars.csv') # Load my data set \n",
    "print(\"First five rows with odd-numbered columns:\")\n",
    "print(cars.iloc[:5, ::2])  # Using iloc to select specific rows and columns \n",
    "                           # :5 value will show the first 5 rows in the data set \n",
    "                           # ::2 which will slice the dataset in columns "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "1a7b007f-9d27-47ad-8b5b-cb98785842aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "1  Mazda RX4 Wag  21.0    6  160.0  110   3.9  2.875  17.02   0   1     4   \n",
       "\n",
       "   carb  \n",
       "1     4  "
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# PART (b)\n",
    "\n",
    "cars = pd.read_csv('cars.csv') # Load my data set \n",
    "cars.loc[[1],['Model','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']]   # Using slicing to get a portion Row 1 of my data set \n",
    "                                                                                                 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "b1b88dc5-d3ed-4f11-94a5-b61eaa444c07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CTLINDER OF THE CAR MODEL CAMARO Z28\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    cyl\n",
       "23    8"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# PART (c)\n",
    "\n",
    "cars = pd.read_csv('cars.csv') # Load my data set \n",
    "print ('CTLINDER OF THE CAR MODEL CAMARO Z28') # Proper labeling \n",
    "cars.loc[(cars['Model']=='Camaro Z28'), ['cyl']] # Indexing used for getting data with conditions ( 1 ROW AND 1 COLUMN OUPUT ONLY ) \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "e112ffd9-6b8c-4b93-862b-c24d81e61a2c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             Model  cyl  gear\n",
      "1    Mazda RX4 Wag    6     4\n",
      "18     Honda Civic    4     4\n",
      "28  Ford Pantera L    8     5\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# PART (d)\n",
    "\n",
    "cars = pd.read_csv('cars.csv') # Load my data set \n",
    "selected_models = cars[ # Storing Values for proper output \n",
    "\n",
    "# Assigning and checking car model to slice the data ----- # extract only the 'Model', 'cylinders' (cyl), and 'gear' from model \n",
    "(cars['Model'] == 'Mazda RX4 Wag') |  (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic') ][['Model', 'cyl', 'gear']]\n",
    "\n",
    "\n",
    "\n",
    "# Print the result\n",
    "print(selected_models)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c3ac8d1-9f92-4b98-ab58-cde5cb033728",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
