import "../../style/elements/bentoCard.css"
import "../../style/main/section.css";
import { useState, useEffect } from "react";
import { FilterBox } from "./filter_box";
import { Table, type StudentData, type AttendanceStatusType } from "./table";
import { supabase } from "../../utils/supabaseClient";
const Attendance = () => {
    const [rawStudents, setRawStudents] = useState<StudentData[]>([]);

    const [searchTerm, setSearchTerm] = useState("");
    const [statusFilter, setStatusFilter] = useState("ALL");
    const [selectedClass, setSelectedClass] = useState("MI3060");

    useEffect(() => {
        const fetchAttendanceData = async () => {
            try {
                // Thực hiện Inner Join trong Supabase: 
                // Lấy bảng attendance nhưng kéo kèm cột student_name từ bảng students thông qua foreign key
                const { data, error } = await supabase
                    .from("attendance")
                    .select(`
                        student_id,
                        status,
                        students (
                            student_name
                        )
                    `)
                    .eq("class_id", selectedClass);

                if (error) throw error;

                if (data) {
                    // Ánh xạ (Map) lại dữ liệu từ cấu trúc Supabase về đúng cấu trúc StudentData của giao diện
                    const formattedData: StudentData[] = data.map((item: any) => ({
                        id: item.student_id,
                        // Giải quyết việc lấy tên từ bảng liên kết (students)
                        name: item.students?.student_name || "Ẩn danh",
                        status: item.status as AttendanceStatusType
                    }));

                    setRawStudents(formattedData);
                }
            } catch (error) {
                console.error("API CALL Error:", error);
            }
        };

        fetchAttendanceData();
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