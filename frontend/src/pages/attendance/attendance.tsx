import React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { BasicTable } from "./table";
import "../../style/elements/bentoCard.css"

const Attendance = () => {
    const [dark, setDark] = React.useState(
        () => document.documentElement.classList.contains('dark') // initial read
    );

    React.useEffect(() => {
        // keep Tailwind dark class in sync
        document.documentElement.classList.toggle('dark', dark);
    }, [dark]);

    const theme = React.useMemo(
        () =>
            createTheme({
                palette: {
                    mode: dark ? 'dark' : 'light',
                },
            }),
        [dark]
    );
    return <ThemeProvider theme={theme}>
        <BasicTable />
    </ThemeProvider>
}

export { Attendance }