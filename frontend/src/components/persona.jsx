import React, { useState, useEffect } from "react";

export default function TablePersona() {
    const [personaList, setPersonaList] = useState([""]);
    const [selectedArcana, setSelectedArcana] = useState("");

    async function AllPersona() {
        const response = await fetch("http://127.0.0.1:8000/list_all");
        const data = await response.json();
        console.log(data);
        setPersonaList(data);
    }

    useEffect(() => {
        AllPersona();
    }, []);

    function handleArcanaChange(evt) {
        setSelectedArcana(evt.target.value);
    }

    return (
        <>
        <h1>Full Persona List</h1>
        <label>
            Arcana:
            <select value={selectedArcana} onChange={handleArcanaChange}>
                <option value="">All</option>
                <option value="Fool">Fool</option>
                <option value="Magician">Magician</option>
                <option value="Priestess">Priestess</option>
                <option value="Empress">Empress</option>
                <option value="Emperor">Emperor</option>
                <option value="Hierophant">Hierophant</option>
                <option value="Lovers">Lovers</option>
                <option value="Chariot">Chariot</option>
                <option value="Justice">Justice</option>
                <option value="Hermit">Hermit</option>
                <option value="Fortune">Fortune</option>
                <option value="Strength">Strength</option>
                <option value="Hanged">Hanged</option>
                <option value="Death">Death</option>
                <option value="Temperance">Temperance</option>
                <option value="Devil">Devil</option>
                <option value="Tower">Tower</option>
                <option value="Star">Star</option>
                <option value="Moon">Moon</option>
                <option value="Sun">Sun</option>
                <option value="Judgement">Judgement</option>
                <option value="Faith">Faith</option>
                <option value="World">Councillor</option>
                <option value="World">All</option>
            </select>
        </label>
        <table>
            <tr>
                <th>Arcana</th>
                <th>Persona Name</th>
                <th>Starting Level</th>
            </tr>
            {personaList
                .filter(persona => selectedArcana === "" || persona.arcana === selectedArcana)
                .map((persona, index) => (
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