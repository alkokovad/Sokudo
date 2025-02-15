import './App.css';
import {Fragment, useEffect, useState} from "react";
import Mapping from "./appMapping/Mapping";
import Profile from "./appProfile/Profile";
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

    const resetState = () => {
        getContent();
    };

    return (
        <Fragment>
            <Mapping content={content} resetState={resetState} />
            <Profile content={content} resetState={resetState} />
        </Fragment>
    );
}

export default App;
