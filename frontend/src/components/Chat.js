import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const Chat = ({ roomName }) => {
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    const socket = io('ws://localhost:8000/ws/chat/' + roomName + '/');

    useEffect(() => {
        socket.on('message', (message) => {
            setMessages((prevMessages) => [...prevMessages, message]);
        });

        return () => {
            socket.off('message');
        };
    }, [roomName]);

    const sendMessage = (e) => {
        e.preventDefault();
        socket.send(JSON.stringify({
            'message': message
        }));
        setMessage('');
    };

    return (
        <div>
            <div>
                {messages.map((message, index) => (
                    <div key={index}>{message}</div>
                ))}
            </div>
            <form onSubmit={sendMessage}>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
};

export default Chat;
