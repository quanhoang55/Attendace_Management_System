
// interface tableElement {

// }


const Table = () => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Student ID</th>
                    <th>Name</th>
                    <th>Status</th>
                </tr>
            </thead>

            <tbody>
                <tr>
                    <td>STU001</td>
                    <td>Nguyen Van A</td>
                    <td>Present</td>
                </tr>
                <tr>
                    <td>STU002</td>
                    <td>Tran Thi B</td>
                    <td>Absent</td>
                </tr>
            </tbody>
        </table>
    )
};

export { Table };