import React from "react";
import "./index.css";
import { App } from "~/components/root/App";
import { createRoot } from 'react-dom/client';
import { OpenAPI } from '~/lib/client';

OpenAPI.BASE = import.meta.env.VITE_API;

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
