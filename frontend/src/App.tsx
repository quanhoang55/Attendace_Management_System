// ============================================================
// IMPORT
// ============================================================
// src/main.tsx
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Stylesheets
// import "./style/main/section.css";
// import "./style/elements/card.css";
import "./style/index.css";

// Components & Layout Layers
import { Header } from "./components/header";
import type { Brand } from "./components/header";

// Pages
// import { Home } from "./pages/home";
// import { DashBoard } from "./pages/dashboard/dashboard";
// import { ChatBot } from "./pages/chatbot/chatbot";

// ============================================================
// MY BRAND
// ============================================================
const MyBrand: Brand = {
  brand_name: "Nhom",
  // brand_logo = "",
  brand_desc: "Personal Project",

  email: "quanhoang1026@gmail.com",
  linkedin: "https://www.linkedin.com/in/ho%C3%A0ng-qu%C3%A2n-652a9b2b0/",
  github: "https://github.com/quanhoang55",

  footer_title: "quanhoang",
  author_name: "quan",
}
const App = () => {

  return (
    <>
      <BrowserRouter>

        <Header myBrand={MyBrand} />
        {/* <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/ChatBot" element={<ChatBot />} />
            <Route path="/DashBoard" element={<DashBoard />} />
          </Routes> */}

      </BrowserRouter>
    </>
  )
}

export { App }
