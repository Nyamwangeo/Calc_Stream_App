{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c197560-b426-46bb-a29a-2dbd66f0f408",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bb81440f-ebfe-4956-aaa2-30365f1cb643",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-30 12:17:38.554 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Paul\\Documents\\New folder\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# Function to calculate compound interest\n",
    "def calculate_compound_interest(principal, rate, times_compounded, years):\n",
    "    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)\n",
    "    return amount\n",
    "\n",
    "# Streamlit app\n",
    "def main():\n",
    "    st.title(\"Compound Interest Calculator\")\n",
    "    \n",
    "    # Sidebar for user inputs\n",
    "    st.sidebar.header(\"User Input Parameters\")\n",
    "    \n",
    "    principal = st.sidebar.number_input(\"Principal Amount ($):\", min_value=0.0, value=1000.0)\n",
    "    rate = st.sidebar.number_input(\"Annual Interest Rate (%):\", min_value=0.0, value=5.0) / 100\n",
    "    times_compounded = st.sidebar.selectbox(\"Compounding Frequency:\", \n",
    "                                            options=[\"Monthly\", \"Semiannually\", \"Annually\"])\n",
    "    \n",
    "    if times_compounded == \"Monthly\":\n",
    "        n = 12\n",
    "    elif times_compounded == \"Semiannually\":\n",
    "        n = 2\n",
    "    else:\n",
    "        n = 1\n",
    "        \n",
    "    years = st.sidebar.number_input(\"Number of Years:\", min_value=0.0, value=10.0)\n",
    "    \n",
    "    # Ensure that n is defined before using it\n",
    "    if st.sidebar.button(\"Calculate\"):\n",
    "        amount = calculate_compound_interest(principal, rate, n, years)\n",
    "        st.success(f\"The future value of the investment: ${amount:.2f}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0024f748-58b9-431b-b74d-17cf9b60759e",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
