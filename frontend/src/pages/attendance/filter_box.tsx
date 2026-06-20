import { AttendanceStatus } from "./table";

interface FilterBoxProps {
    searchTerm: string;
    onSearchChange: (value: string) => void;
    statusFilter?: string;
    onStatusFilterChange?: (value: string) => void;
}

const FilterBox = ({
    searchTerm,
    onSearchChange,
    // statusFilter,
    // onStatusFilterChange
}: FilterBoxProps) => {
    return (
        <div className="section__header">
            <div className="">
                <label htmlFor="studentSearch">
                    Chọn Lớp Học
                </label>
                <input
                    id="studentSearch"
                    type="text"
                    placeholder="Nhập Mã Lớp"
                    value={searchTerm}
                    onChange={(e) => onSearchChange(e.target.value)}
                />
            </div>

            {/* <div className="filter-group">
                <label htmlFor="statusFilterSelect" className="filter-label">
                    Lọc theo trạng thái
                </label>
                <select
                    id="statusFilterSelect"
                    value={statusFilter}
                    onChange={(e) => onStatusFilterChange(e.target.value)}
                    className="bento-dropbox"
                >
                    <option value="ALL">Tất cả trạng thái</option>
                    <option value={AttendanceStatus.None}>Chưa cập nhật</option>
                    <option value={AttendanceStatus.Present}>Có Mặt</option>
                    <option value={AttendanceStatus.Excused}>Vắng Có Phép</option>
                    <option value={AttendanceStatus.Unexcused}>Vắng Không Phép</option>
                </select>
            </div> */}

        </div>
    );
};

export { FilterBox };