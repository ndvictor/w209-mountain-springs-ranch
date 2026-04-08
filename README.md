# Course

## DATASCI 209: Data Visualization
## UC Berkeley School of Information

# Mountain Springs Ranch Cattle Movement Visualization

This project is an interactive data visualization created for **DATASCI 209: Data Visualization** at the **UC Berkeley School of Information**.

It visualizes how cattle groups move across the different ranch locations of **Mountain Springs Ranch** over the course of a year. The goal is to help users understand **seasonal herd distribution** and observe how cattle move across ranch units over time.

## Project Overview

Mountain Springs Ranch is a large cow-calf cattle operation in central Idaho, with herds distributed across many non-contiguous locations. Different land units are used seasonally, and different herds specialize in different cattle types.

Our visualization combines:

- spatial context through a ranch map
- temporal exploration through animation and a time slider
- categorical detail through cattle-type encodings
- daily herd state reconstruction from narrative movement data

The result is an interactive tool that allows users to:

- visualize seasonal herd distribution
- show movement across ranch locations over time
- track where cattle are located on a selected date
- compare herd composition across locations and seasons

## Features

- Interactive Observable visualization embedded into a project website
- Playable time-based animation of herd movement
- Date-based exploration of cattle distribution
- Ranch map showing herd locations
- Visual encoding of cattle type and head count
- Project website with explanatory narrative, design process, usability notes, and team information

## Data Sources

The project is based on two main data sources:

- **Ranch valuation map**
- **Range manager narrative**

These inputs were transformed into a machine-readable daily ranch state table so that cattle locations could be visualized consistently across time.

## Tech Stack

- **Flask**
- **HTML**
- **CSS**
- **JavaScript**
- **Observable**
- **Vercel**

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── vercel.json
├── templates/
│   └── w209.html
├── static/
│   ├── team/
│   └── ranch-hero.mp4
└── README.md
```
## Local Devopment

Clone the repo and run locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask --app app.py --debug run
```
Then open:

```bash
http://127.0.0.1:5000
```

## Deployment

This project is configured for deployment on Vercel using Flask.

## Team Members

- Alec Heyde
- Brian Jaffe
- Ewura Mensah
- Victor Ndayambaje