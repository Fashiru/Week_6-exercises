{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2074f03c-9cbe-4c30-8e69-904327ca29b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# WELCOME to the Name Game\n",
    "You are welcome to the \"Name Game\". In this notebook, we will learn how to play the Name Game using python. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "352ca9ac-374a-4691-ae14-207ac38c8c19",
   "metadata": {},
   "outputs": [],
   "source": [
    "#What is the \"Name Game\"\n",
    "The Name game is a playful song where each name is transformed into a fun version of itself. In this game, you take a person's name and modify it according to a set of rules:\n",
    "* The first letter of the name is repeated.\n",
    "* The name is rhymed with various sounds like \"ba\", \"fa\", etc.\n",
    "* The game can be sung and played by kids, often in school.\n",
    "Example: Damon, Damon, Devil-melon\n",
    "killed a chicken and became a felon\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "019f6dfb-e9a8-4d24-957a-6c295449acd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def name_game(name):\n",
    "    name = name.lower()\n",
    "    first_letter = name[0]\n",
    "    modified_name = f\"{first_letter}-{first_letter}-{name}\"\n",
    "    return modified_name.capitalize()\n",
    "\n",
    "print(name_game(\"Damon\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66e076e5-21f6-4beb-ad48-17997222a639",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(name_game(\"Amanda\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c139e218-029a-4705-a2e6-dcdf54fc3030",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'name_game' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[4], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[43mname_game\u001b[49m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCharlie\u001b[39m\u001b[38;5;124m\"\u001b[39m))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'name_game' is not defined"
     ]
    }
   ],
   "source": [
    "print(name_game(\"Charlie\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ff13192-52b9-48ce-b512-dbb58853be73",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75669a8e-da1f-4a50-8446-3f6f5c4a169f",
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
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
