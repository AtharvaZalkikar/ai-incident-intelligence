import { useRef } from "react";
import { Upload } from "lucide-react";
import { uploadLogs } from "../services/uploadService";

export default function UploadBox({ onUploadSuccess }) {

    const inputRef = useRef();

    async function handleFile(file) {

        if (!file) return;

        try {

            await uploadLogs(file);

            onUploadSuccess();

        } catch (err) {

            console.error(err);

            alert("Upload failed");

        }

    }

    return (

        <div className="mx-auto mt-8 max-w-7xl px-8">

            <div
                className="cursor-pointer rounded-xl border border-dashed border-slate-700 bg-slate-900 p-10 text-center transition hover:border-cyan-400"
                onClick={() => inputRef.current.click()}
            >

                <Upload
                    size={60}
                    className="mx-auto mb-5 text-cyan-400"
                />

                <h2 className="text-2xl font-semibold">

                    Upload Investigation

                </h2>

                <p className="mt-3 text-slate-400">

                    Drag & Drop or click to select log files

                </p>

                <p className="mt-2 text-sm text-slate-500">

                    CSV files supported

                </p>

            </div>

            <input
                type="file"
                accept=".csv"
                hidden
                ref={inputRef}
                onChange={(e) => handleFile(e.target.files[0])}
            />

        </div>

    );

}