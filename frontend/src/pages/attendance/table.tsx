import { Fragment } from "react";
import "../../style/elements/bentoCard.css"
import "../../style/main/section.css";

// ==========================================================================
// TYPE DEFINITIONS & CONSTANTS
// ==========================================================================
export const AttendanceStatus = {
    Present: "CM",
    Excused: "VCP",
    Unexcused: "VKP",
    None: "NONE" // Đã thêm trạng thái Chưa cập nhật vào Object hằng số
} as const;

export type AttendanceStatusType = typeof AttendanceStatus[keyof typeof AttendanceStatus];

export interface StudentData {
    id: string;
    name: string;
    status: AttendanceStatusType;
}

// ==========================================================================
// ROW COMPONENT
// ==========================================================================
interface RowProps {
    student: StudentData;
    onStatusChange: (id: string, newStatus: AttendanceStatusType) => void;
}

const Row = ({ student, onStatusChange }: RowProps) => {
    return (
        <tr className="bento__body">
            <td>{student.id}</td>
            <td>{student.name}</td>
            <td>
                <select
                    name="attendanceStatus"
                    value={student.status}
                    onChange={(e) => onStatusChange(student.id, e.target.value as AttendanceStatusType)}
                    className="bento-dropbox"
                    aria-label={`Điểm danh cho ${student.name}`}
                >
                    <option value={AttendanceStatus.None}>Chưa cập nhật</option>
                    <option value={AttendanceStatus.Present}>Có Mặt</option>
                    <option value={AttendanceStatus.Excused}>Vắng Có Phép</option>
                    <option value={AttendanceStatus.Unexcused}>Vắng Không Phép</option>
                </select>
            </td>
        </tr>
    );
};

export { Row };

// ==========================================================================
// TABLE COMPONENT
// ==========================================================================
interface TableProps {
    students: StudentData[];
    onStatusChange: (id: string, newStatus: AttendanceStatusType) => void;
}

const Table = ({ students, onStatusChange }: TableProps) => {
    return (
        <table className="bento-card">
            <thead>
                <tr className="bento__header">
                    <th>Student ID</th>
                    <th>Name</th>
                    <th>Status</th>
                </tr>
            </thead>

            <tbody>
                {students.length === 0 ? (
                    <tr className="bento__body">
                        <td colSpan={3}>
                            Không tìm thấy sinh viên hợp lệ.
                        </td>
                    </tr>
                ) : (
                    students.map((student, index) => (
                        <Fragment key={student.id}>
                            <Row
                                student={student}
                                onStatusChange={onStatusChange} />
                            {index < students.length - 1 && (
                                <tr>
                                    <td colSpan={3}>
                                        <hr className="bento-table__divider" />
                                    </td>
                                </tr>
                            )}
                        </Fragment>
                    ))
                )}
            </tbody>
        </table>
    );
};

export { Table };