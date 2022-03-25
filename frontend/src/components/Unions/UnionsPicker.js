
import { useState, useEffect } from "react";
import M from "materialize-css";

export default function UnionsPicker() {

    const [unions, setUnions] = useState(null)

    useEffect(() => {
        M.AutoInit();
    }, [unions]);

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
            <span className="preloader-wrapper small active">
                <div className="spinner-layer spinner-red-only">
                    <div className="circle-clipper left">
                        <div className="circle"></div>
                    </div><div className="gap-patch">
                        <div className="circle"></div>
                    </div><div className="circle-clipper right">
                        <div className="circle"></div>
                    </div>
                </div>
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
