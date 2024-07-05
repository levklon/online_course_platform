import React, { useState, useEffect } from 'react';
import axios from 'axios';
import VideoPlayer from './VideoPlayer';
import Checkout from './Checkout';
import StyledButton from './StyledButton'; 
import LazyImage from './LazyImage'; 


const CourseDetail = ({ match }) => {
    const [course, setCourse] = useState(null);
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        const fetchCourse = async () => {
            const result = await axios(`/api/courses/${match.params.id}/`);
            setCourse(result.data);
            setVideos(result.data.videos);
        };
        fetchCourse();
    }, [match.params.id]);

    return (
        <div>
            {course && (
                <div>
                    <h1>{course.title}</h1>
                    <p>{course.description}</p>
                    <div>
                        {videos.map(video => (
                            <VideoPlayer key={video.id} url={video.url} />
                        ))}
                    </div>
                    <LazyImage src="path_to_image" alt="Course Image" /> {/* LazyImage */}
                    <Checkout />
                    <StyledButton />
                </div>
            )}
        </div>
    );
};

export default CourseDetail;