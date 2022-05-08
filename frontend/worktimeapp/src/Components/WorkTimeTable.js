import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';

function createData(name, projects) {
    return {
        name,
        projects: [
            {
                projectName: 'Project A',
                activity: 'Use Case erstellen',
                date: '2020-01-02',
                employee: 'Max Mustermann',
                plannedTime: 3,
                bookedTime: 1,
            },
            {
                projectName: 'Project A',
                activity: 'Use Case erstellen',
                date: '2020-01-02',
                employee: 'Max Musterfrau',
                plannedTime: 14,
                bookedTime: 5,
            },
        ],
    };
}

function Row(props) {
    const { row } = props;
    const [open, setOpen] = React.useState(false);


    return (
        <React.Fragment>
            <TableRow sx={{ '& > *': { borderBottom: 'unset' } }}>
                <TableCell>
                    <IconButton
                        aria-label="expand row"
                        size="small"
                        onClick={() => setOpen(!open)}
                    >
                        {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                    </IconButton>
                </TableCell>
                <TableCell component="th" scope="row" >
                    {row.name} X
                </TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
            </TableRow>
            <TableRow>
                <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                    <Collapse in={open} timeout="auto" unmountOnExit>
                        <Box sx={{ margin: 0.5 }}>
                            <Typography variant="h6" gutterBottom component="div">
                                Detailed View
                            </Typography>
                            <Table size="small" aria-label="purchases">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>Activity</TableCell>
                                        <TableCell>Date</TableCell>
                                        <TableCell>Employee</TableCell>
                                        <TableCell align="right">Planned time (h)</TableCell>
                                        <TableCell align="right">Booked Time (h)</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {row.projects.map((projectsRow) => (
                                        <TableRow key={projectsRow}>
                                            <TableCell>{projectsRow.activity}</TableCell>
                                            <TableCell component="th" scope="row">
                                                {projectsRow.date}
                                            </TableCell>
                                            <TableCell>{projectsRow.employee}</TableCell>
                                            <TableCell align="right">{projectsRow.plannedTime}</TableCell>
                                            <TableCell align="right">
                                                {projectsRow.bookedTime}
                                            </TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </Box>
                    </Collapse>
                </TableCell>
            </TableRow>
        </React.Fragment>
    );
}



const rows = [
    createData('Project A', 'Use Case'),
    createData('Project B'),
    createData('Project C'),
    createData('Project D'),
    createData('Project E'),
];

export default function CollapsibleTable() {
    return (
        <TableContainer component={Paper}>
            <Table aria-label="collapsible table">
                <TableHead>
                    <TableRow>
                        <TableCell />
                        <TableCell>Project Overview</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row) => (
                        <Row key={row.name} row={row} />
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}
