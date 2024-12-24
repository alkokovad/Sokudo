import './App.css';
import {Fragment, useEffect, useState} from "react";
// import Header from "./appHeader/Header";
import axios from "axios";
import {API_URL} from "./index";

function App() {
    const [content, setContent] = useState([])

    useEffect(() => {
        getContent()
    }, [])

    const getContent = (data) => {
        axios.get(API_URL).then(data => setContent(data.data))
    }

    return (
        <Fragment>
            <iframe title="map" srcdoc={content}></iframe>
        </Fragment>
    );
}

export default App;
