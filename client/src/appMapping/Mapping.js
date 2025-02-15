import './mapping.css';
import {useEffect, useState} from "react";
import axios from "axios";
import {API_URL} from "../index";

const Mapping = () => {
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
        <iframe id="map" title="map" srcDoc={content}></iframe>
    )
}

export default Mapping;