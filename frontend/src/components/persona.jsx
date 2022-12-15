import React, { useState, useEffect } from "react";

export default function TablePersona() {
    const [personaList, setPersonaList] = useState([""]);

    async function AllPersona() {
        const response = await fetch("http://127.0.0.1:8000/list_all");
        const data = await response.json();
        console.log(data);
        setPersonaList(data);
    }

    useEffect(() => {
        AllPersona();
    }, []);

    return (
        <>
        <h1>Full Persona List</h1>
        <table>
            <tr>
                <th>Arcana</th>
                <th>Persona Name</th>
                <th>Starting Level</th>
            </tr>
            {personaList.map((persona, index) => (
            <tr key={index}>
                <td>{persona.arcana}</td>
                <td>{persona.persona_name}</td>
                <td>{persona.starting_level}</td>
            </tr>
            ))}
        </table>
        </>
    );
}