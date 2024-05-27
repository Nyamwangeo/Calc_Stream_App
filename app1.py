{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "30a0fda8-a98d-4975-bacc-8cd67c289e18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (1.30.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (7.0.1)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (2.0.1)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (10.2.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: pyarrow>=6.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (14.0.2)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (13.3.5)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (4.9.0)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (2.1)\n",
      "Requirement already satisfied: validators<1,>=0.2 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (0.18.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (3.1.37)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (6.3.3)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.17.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from validators<1,>=0.2->streamlit) (5.1.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\paul\\documents\\new folder\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5a381fbb-3069-43fd-8639-d588bf10531d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-05-27 14:25:32.109 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Paul\\Documents\\New folder\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import math\n",
    "\n",
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
   "id": "07d50b6c-8a7c-465d-9f35-b9cd4db8f423",
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
