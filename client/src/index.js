import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

export const API_URL = "http://localhost:8001/api/service/"
export const API_STATIC_MEDIA = "http://localhost:8001/"
// export const API_URL = "http://sain-customs.ru/api/content/"
// export const API_STATIC_MEDIA = "http://sain-customs.ru/"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
);

reportWebVitals();