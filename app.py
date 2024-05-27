{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "954ba398-ad1f-4bea-ae9b-af2e2541cf00",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import math\n",
    "\n",
    "# Function to calculate compound interest\n",
    "def calculate_compound_interest(principal, rate, times_compounded, years):\n",
    "    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)\n",
    "    return amount\n",
    "\n",
    "# Function to calculate z-score\n",
    "def calculate_z_score(x, mean, stdev):\n",
    "    z = (x - mean) / stdev\n",
    "    return z\n",
    "\n",
    "# Streamlit app\n",
    "def main():\n",
    "    st.title(\"Financial and Statistical Calculator\")\n",
    "    \n",
    "    # Compound Interest Calculator\n",
    "    st.header(\"Compound Interest Calculator\")\n",
    "    \n",
    "    principal = st.number_input(\"Principal Amount ($):\", min_value=0.0, value=1000.0)\n",
    "    rate = st.number_input(\"Annual Interest Rate (%):\", min_value=0.0, value=5.0) / 100\n",
    "    times_compounded = st.number_input(\"Times Compounded Per Year:\", min_value=1, value=4)\n",
    "    years = st.number_input(\"Number of Years:\", min_value=0.0, value=10.0)\n",
    "    \n",
    "    if st.button(\"Calculate Compound Interest\"):\n",
    "        amount = calculate_compound_interest(principal, rate, times_compounded, years)\n",
    "        st.success(f\"The future value of the investment: ${amount:.2f}\")\n",
    "    \n",
    "    # Z-Score Calculator\n",
    "    st.header(\"Z-Score Calculator\")\n",
    "    \n",
    "    x = st.number_input(\"Value (x):\", value=0.0)\n",
    "    mean = st.number_input(\"Mean (μ):\", value=0.0)\n",
    "    stdev = st.number_input(\"Standard Deviation (σ):\", value=1.0)\n",
    "    \n",
    "    if st.button(\"Calculate Z-Score\"):\n",
    "        z = calculate_z_score(x, mean, stdev)\n",
    "        st.success(f\"The Z-Score is: {z:.2f}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a26abe65-bfe9-4cbd-9ef0-ef95fecaa63d",
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
