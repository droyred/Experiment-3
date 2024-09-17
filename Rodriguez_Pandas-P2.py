{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "027e3195-9945-48f5-993d-4fa45ae61683",
   "metadata": {},
   "source": [
    "# EXPERIMENT 3 - RODRIGUEZ, Andrei Joshua\n",
    "I. Intended Learning Outcomes:\n",
    "1. To identify the codes and functions incorporated in the Pandas library\n",
    "2. To be able to apply and use the different codes and functions in creating a Python program using a\n",
    "Pandas library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7cd6a11c-dc0a-41ef-b810-fc7b8c630940",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "77ef0a98-28a7-44c8-baaa-89cc18db1b61",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Here we load the CSV file into our notebook...\n",
    "cars = pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "636e2768-e6ca-42ab-b35e-3139fd0f2e67",
   "metadata": {},
   "source": [
    "**a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ed6e365f-131a-4de9-bba7-428c6878bb83",
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
       "      <th>mpg</th>\n",
       "      <th>disp</th>\n",
       "      <th>drat</th>\n",
       "      <th>qsec</th>\n",
       "      <th>am</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>21.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>3.90</td>\n",
       "      <td>16.46</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>21.0</td>\n",
       "      <td>160.0</td>\n",
       "      <td>3.90</td>\n",
       "      <td>17.02</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>22.8</td>\n",
       "      <td>108.0</td>\n",
       "      <td>3.85</td>\n",
       "      <td>18.61</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>21.4</td>\n",
       "      <td>258.0</td>\n",
       "      <td>3.08</td>\n",
       "      <td>19.44</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>18.7</td>\n",
       "      <td>360.0</td>\n",
       "      <td>3.15</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    mpg   disp  drat   qsec  am  carb\n",
       "0  21.0  160.0  3.90  16.46   1     4\n",
       "1  21.0  160.0  3.90  17.02   1     4\n",
       "2  22.8  108.0  3.85  18.61   1     1\n",
       "3  21.4  258.0  3.08  19.44   0     1\n",
       "4  18.7  360.0  3.15  17.02   0     2"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odd_columns = cars.iloc[:, 1::2].head(5)\n",
    "odd_columns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f62fcd5e-44d7-4e71-9781-9599b9b3caae",
   "metadata": {},
   "source": [
    "**b. Display the row that contains the ‘Model’ of ‘Mazda RX4’**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "4318cf11-565d-470d-a9ac-7a74cc03c369",
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
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
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
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mazda_rx4_row = cars[cars['Model'] == 'Mazda RX4']\n",
    "mazda_rx4_row"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "685a0640-3ebd-4e7f-9ab0-07ae5085558d",
   "metadata": {},
   "source": [
    "**c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "81d48965-f4e6-466f-95bd-ca8ccfd5eac9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "camaro_z28_cyl = cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0]\n",
    "camaro_z28_cyl"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bafef4b7-79ee-46d7-b8cf-0f883e61c2fc",
   "metadata": {},
   "source": [
    "**d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4\n",
    "Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f1715257-6338-42bb-9c54-bcb54938a9a0",
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
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "specific_models = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])][['Model', 'cyl', 'gear']]\n",
    "specific_models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e85758a-c20b-41ed-8596-0f6830332579",
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
