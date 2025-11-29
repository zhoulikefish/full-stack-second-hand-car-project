# Used Car Trading Platform

A comprehensive full-stack web application for used car trading, featuring intelligent price prediction, market analysis, and user management capabilities.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Machine Learning Models](#machine-learning-models)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This platform provides a comprehensive solution for the used car market, integrating web scraping, machine learning-based price prediction, and a user-friendly interface for browsing and managing car listings. The system leverages data from major Chinese automotive websites to provide accurate market insights and price forecasts.

## ✨ Features

### Core Functionality
- **User Authentication & Authorization**: Secure JWT-based authentication system
- **Car Listing Management**: Browse, search, and filter used car listings
- **Favorites System**: Save and manage favorite car listings
- **User Profiles**: Personalized user accounts with activity tracking

### Advanced Features
- **Intelligent Price Prediction**: ML-powered price estimation based on multiple parameters
- **Time Series Forecasting**: Predict future price trends using macroeconomic indicators
- **Car Evaluation**: Comprehensive vehicle valuation system
- **Market Analytics Dashboard**: Visualize market trends and statistics
- **Popular Cars Section**: Discover trending vehicles in the market
- **Image Upload**: Support for car image management
- **Geographic Analysis**: China map integration for regional market insights

### Data Collection
- **Web Scraping**: Automated data collection from major automotive platforms
  - AutoHome
  - Icauto 

## 🛠 Tech Stack

### Frontend
- **Framework**: Vue.js 2.7
- **UI Library**: Element UI
- **State Management**: Vuex
- **Routing**: Vue Router
- **HTTP Client**: Axios
- **Authentication**: JWT Decode

### Backend
- **Runtime**: Node.js
- **Framework**: Express.js
- **Database**: MongoDB with Mongoose ODM
- **Authentication**: Passport.js with JWT Strategy
- **Password Encryption**: Bcrypt
- **File Upload**: Multer
- **Remote Execution**: SSH2

### Machine Learning
- **Language**: Python 3.x
- **Core Libraries**:
  - XGBoost
  - LightGBM
  - Pandas
  - NumPy
  - Scikit-learn
  - Joblib

### Web Scraping
- **Framework**: Scrapy
- **Data Sources**: AutoHome, Icauto

##  Project Structure

```
KeChengSheJi_Group2/
├── backend/                    # Backend API server
│   ├── config/                 # Configuration files
│   │   ├── keys.js            # Database and JWT keys
│   │   └── passport.js        # Passport authentication config
│   ├── models/                 # Mongoose data models
│   │   ├── Car.js             # Car listing model
│   │   ├── User.js            # User model
│   │   ├── Like.js            # Favorites model
│   │   └── Popular.js         # Popular cars model
│   ├── routes/api/            # API route handlers
│   │   ├── users.js           # User authentication routes
│   │   ├── cars.js            # Car listing routes
│   │   ├── likes.js           # Favorites routes
│   │   ├── populars.js        # Popular cars routes
│   │   ├── imgs.js            # Image upload routes
│   │   └── pyscripts.js       # ML prediction routes
│   ├── pyscripts/             # Python ML scripts
│   │   ├── evaluate/          # Car evaluation model
│   │   │   ├── main.py        # Price evaluation script
│   │   │   ├── dataset/       # Training and test data
│   │   │   └── model/         # Trained ML models
│   │   ├── timeseries/        # Time series forecasting
│   │   │   ├── main_macro.py  # Macro-economic forecasting
│   │   │   ├── dataset/       # Economic indicators data
│   │   │   └── model/         # Time series models
│   │   └── func_evaluate.py   # Evaluation utilities
│   ├── utils/                 # Utility functions
│   │   └── auth.js            # Authentication helpers
│   ├── server.js              # Express server entry point
│   └── package.json           # Backend dependencies
│
├── frontend/client/           # Vue.js frontend application
│   ├── public/                # Static public assets
│   ├── src/
│   │   ├── assets/            # Images, fonts, and styles
│   │   ├── components/        # Reusable Vue components
│   │   │   ├── HeadNav.vue    # Navigation bar
│   │   │   ├── FilterPrice.vue # Price filtering
│   │   │   ├── ChinaMap.vue   # Geographic visualization
│   │   │   └── ...
│   │   ├── views/             # Page components
│   │   │   ├── Home.vue       # Homepage
│   │   │   ├── Login.vue      # Login page
│   │   │   ├── Register.vue   # Registration page
│   │   │   ├── CarDetails.vue # Car details page
│   │   │   ├── Evaluate.vue   # Price evaluation page
│   │   │   ├── PricePredict.vue # Price prediction
│   │   │   ├── Board.vue      # Analytics dashboard
│   │   │   ├── Search.vue     # Search page
│   │   │   └── ...
│   │   ├── router.js          # Route configuration
│   │   ├── store.js           # Vuex store
│   │   ├── http.js            # Axios configuration
│   │   └── main.js            # Application entry point
│   ├── dist/                  # Production build output
│   ├── package.json           # Frontend dependencies
│   └── vue.config.js          # Vue CLI configuration
│
└── web_scrapy/                # Web scraping modules
    ├── Autohome crawl/           # AutoHome scraper
    │   └── Crawler/
    └── Icauto crawl/         # Icauto scraper
        └── Crawler/
```

##  Prerequisites

- **Node.js** (v14.x or higher)
- **npm** or **yarn**
- **MongoDB** (v4.x or higher)
- **Python** (v3.7 or higher)
- **pip** (Python package manager)

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/KeChengSheJi_Group2.git
cd KeChengSheJi_Group2
```

### 2. Backend Setup

```bash
cd backend
npm install
```

### 3. Frontend Setup

```bash
cd frontend/client
npm install
```

### 4. Python Dependencies

```bash
cd backend/pyscripts
pip install -r requirements.txt
```

Required Python packages:
- xgboost
- lightgbm
- pandas
- numpy
- scikit-learn
- joblib

##  Configuration

### Backend Configuration

Create or modify `backend/config/keys.js`:

```javascript
module.exports = {
  mongoURI: "mongodb://localhost:27017/usedcar",
  secretOrKey: "your-secret-key"
};
```

### Frontend Configuration

Update API endpoint in `frontend/client/src/http.js` if needed:

```javascript
axios.defaults.baseURL = 'http://localhost:5000/api';
```

##  Usage

### Development Mode

#### Start Backend Server
```bash
cd backend
npm run server
```
Backend will run on `http://localhost:5000`

#### Start Frontend Development Server
```bash
cd frontend/client
npm run serve
```
Frontend will run on `http://localhost:8080`

#### Run Both Concurrently
```bash
cd backend
npm run dev
```

### Production Mode

#### Build Frontend
```bash
cd frontend/client
npm run build
```

#### Start Production Server
```bash
cd backend
npm start
```

##  API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/users/register` | Register new user | No |
| POST | `/api/users/login` | User login | No |
| GET | `/api/users/current` | Get current user | Yes |

### Car Listing Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/cars` | Get all car listings | No |
| GET | `/api/cars/:id` | Get car by ID | No |
| POST | `/api/cars` | Create new listing | Yes |
| PUT | `/api/cars/:id` | Update listing | Yes |
| DELETE | `/api/cars/:id` | Delete listing | Yes |

### Favorites Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/likes` | Get user favorites | Yes |
| POST | `/api/likes` | Add to favorites | Yes |
| DELETE | `/api/likes/:id` | Remove from favorites | Yes |

### Machine Learning Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/pyscripts/evaluate` | Evaluate car price | No |
| POST | `/api/pyscripts/forecast` | Predict price trends | No |

### Image Upload Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/imgs/upload` | Upload car images | Yes |

##  Machine Learning Models

### Price Evaluation Model

Located in `backend/pyscripts/evaluate/`

**Features**:
- Province and location
- Brand and model
- License year and update time
- Mileage
- Engine displacement
- Number of transfers
- Electric vehicle parameters (range, charge time, battery capacity)

**Models Used**:
- XGBoost (for maximum and minimum price)
- LightGBM (for maximum and minimum price)
- Ensemble weighting for final prediction

### Time Series Forecasting Model

Located in `backend/pyscripts/timeseries/`

**Features**:
- Historical price data
- Macroeconomic indicators (GDP, fuel prices, deals volume)
- Temporal features

**Models Used**:
- XGBoost time series model
- LightGBM time series model
- Weighted ensemble for forecast

### Model Training Data

Training datasets are included in:
- `backend/pyscripts/evaluate/dataset/`
- `backend/pyscripts/timeseries/dataset/`

Pre-trained models are stored in:
- `backend/pyscripts/evaluate/model/`
- `backend/pyscripts/timeseries/model/`
---

**Note**: This is a course design project developed by Group 2. The application demonstrates the integration of modern web technologies with machine learning for practical business applications in the used car trading market.
