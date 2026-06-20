import "../../style/elements/bentoCard.css"
import "../../style/main/section.css";
import { useState, useEffect } from "react";
import { FilterBox } from "./filter_box";
import { Table, type StudentData } from "./table";
const Attendance = () => {
    const [rawStudents, setRawStudents] = useState<StudentData[]>([]);

    const [searchTerm, setSearchTerm] = useState("");
    const [statusFilter, setStatusFilter] = useState("ALL");
    const [selectedClass, setSelectedClass] = useState("MI3060");

    useEffect(() => {
        const fetchStudentsByClass = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/students?class_id=${selectedClass}`);
                const data = await response.json();
                setRawStudents(data);
            } catch (error) {
                console.error("Call API Error:", error);
                // Nếu lỗi, tạm thời dùng dữ liệu giả của bạn để test giao diện
                setRawStudents([
                    { id: "STU001", name: "Nguyen Van A", status: "CM" },
                    { id: "STU002", name: "Tran Thi B", status: "VCP" },
                    { id: "STU003", name: "Le Van C", status: "VKP" },
                    { id: "STU003", name: "Le Van C", status: "NONE" }
                ]);
            }
        };
        fetchStudentsByClass();
    }, [selectedClass]);

    const displayedStudents = rawStudents
        .filter(student => {
            // Lọc theo tên hoặc mã sinh viên
            const matchesSearch = student.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                student.id.toLowerCase().includes(searchTerm.toLowerCase());

            // Lọc theo trạng thái điểm danh
            const matchesStatus = statusFilter === "ALL" || student.status === statusFilter;

            return matchesSearch && matchesStatus;
        })
        .sort((a, b) => a.id.localeCompare(b.id)); // Sắp xếp theo ID sinh viên tăng dần

    // 5. Hàm cập nhật trạng thái (giữ nguyên logic map của bạn)
    const handleStatusChange = (id: string, newStatus: StudentData["status"]) => {
        setRawStudents(prev =>
            prev.map(student => student.id === id ? { ...student, status: newStatus } : student)
        );
        // Ở đây bạn có thể gọi thêm một hàm API POST/PATCH để lưu trạng thái này vào Supabase ngay lập tức
    };

    return (
        <main>
            <section className="section section--surface">
                <div className="section__header ">
                    <h1 className="section__title">Attendance Record</h1>
                </div>
                <div className="container">

                    <FilterBox
                        searchTerm={searchTerm}
                        onSearchChange={setSearchTerm}
                        statusFilter={statusFilter}
                        onStatusFilterChange={setStatusFilter}
                    />
                    <Table
                        students={displayedStudents}
                        onStatusChange={handleStatusChange}
                    />
                </div>
            </section>
        </main>
    )
}

export { Attendance }