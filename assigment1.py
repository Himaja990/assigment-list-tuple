{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "87490512",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n",
      "[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]\n"
     ]
    }
   ],
   "source": [
    "'''\n",
    "Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples\n",
    "\n",
    "\n",
    "\n",
    "Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]\n",
    "\n",
    "Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]\n",
    "\n",
    "\n",
    "'''\n",
    "\n",
    "tuple1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]\n",
    "List2=[]\n",
    "List3=[]\n",
    "\n",
    "for t in tuple1:\n",
    "    List2.append(t[1],)\n",
    "    \n",
    "List2.sort()\n",
    "print(List2)\n",
    "\n",
    "for i in List2:\n",
    "    for j in tuple1:\n",
    "        if i == int(j[1],):\n",
    "            List3.append(j)\n",
    "print(List3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a867a576",
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
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
