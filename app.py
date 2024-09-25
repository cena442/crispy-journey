{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "from PIL import Image\n",
    "import streamlit as st\n",
    "\n",
    "\n",
    "\n",
    "pickle_in = open(r\"finalized_model_1.sav\", \"rb\")\n",
    "classifier=pickle.load(pickle_in)\n",
    "\n",
    "def welcome():\n",
    "    return \"Welcome All\"\n",
    "\n",
    "\n",
    "def iris_flower_prediction(sepal_length,sepal_width,petal_length,petal_width):\n",
    "    \n",
    "    sepal_length = float(sepal_length)\n",
    "    sepal_width = float(sepal_width)\n",
    "    petal_length = float(petal_length)\n",
    "    petal_width = float(petal_width)\n",
    "\n",
    "   \n",
    "    prediction=classifier.predict([[sepal_length,sepal_width,petal_length,petal_width]])\n",
    "    print(prediction)\n",
    "    return prediction\n",
    "\n",
    "\n",
    "\n",
    "def main():\n",
    "    st.title(\"Iris Flower Predictor\")\n",
    "    html_temp = \"\"\"\n",
    "    <div style=\"background-color:tomato;padding:10px\">\n",
    "    <h2 style=\"color:white;text-align:center;\">Iris Flower Predictor </h2>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    st.markdown(html_temp,unsafe_allow_html=True)\n",
    "    sepal_length = st.text_input(\"sepal_length\",\"Type Here\")\n",
    "    sepal_width = st.text_input(\"sepal_width\",\"Type Here\")\n",
    "    petal_length = st.text_input(\"petal_length\",\"Type Here\")\n",
    "    petal_width = st.text_input(\"petal_width\",\"Type Here\")\n",
    "    result=\"\"\n",
    "    if st.button(\"Predict\"):\n",
    "        result= iris_flower_prediction(sepal_length,sepal_width,petal_length,petal_width)\n",
    "    st.success('The output is {}'.format(result))\n",
    "    if st.button(\"About\"):\n",
    "        st.text(\"Lets LEarn\")\n",
    "        st.text(\"Built with Streamlit\")\n",
    "\n",
    "if __name__=='main_':\n",
    "    main()"
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
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
