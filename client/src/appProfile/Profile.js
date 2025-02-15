import './profile.css';
import {useEffect, useState} from "react";
import axios from "axios";
import {API_URL} from "../index";

const Profile = () => {
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
        <button className="profile_btn">
            <img className="profile_pic" src={"media/profile.png"}/>
        </button>
    )
}

export default Profile;