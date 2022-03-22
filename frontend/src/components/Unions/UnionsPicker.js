import React from "react"
import { useState, useEffect } from "react";
import { FaSpinner } from "react-icons/fa";

export default function UnionsPicker() {

    const [unions, setUnions] = useState(null)

    useEffect(() => {

        async function getUnions() {
            const r = await fetch("http://localhost:18083/unions");
            const payload = await r.json();
            setUnions(payload);
        }
        getUnions();
    }, []);

    const [unionIndex, setUnionIndex] = useState(() => {
        const storedUnionIndex = window.localStorage.getItem("unionIndex");
        return storedUnionIndex ? storedUnionIndex : 0
    });

    useEffect(() => {
        const storedUnionIndex = window.localStorage.getItem("unionIndex");
        if (storedUnionIndex) {
            setUnionIndex(storedUnionIndex);
        }
    }, []);

    useEffect(() => {
        window.localStorage.setItem("unionIndex", unionIndex);
    }, [unionIndex]);

    if (unions === null) {
        return (
            <span>
                <FaSpinner className="icon-loading" />
            </span>
        )
    }

    return (
        <select onChange={(e) => setUnionIndex(e.target.value)}>
            {unions.map((u, i) => (
                <option
                    className={i === unionIndex ? "selected" : null}
                    value={i}
                    key={u.id}
                >
                    {u.name}
                </option>
            ))
            }
        </select >
    );
}
