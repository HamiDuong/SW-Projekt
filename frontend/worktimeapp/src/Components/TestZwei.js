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
import { Button } from '@mui/material';


function createData(name, activities, employee, planedTime, bookedTime, searchedFor) {
    return {
        name,
        activities,
        employee,
        planedTime,
        bookedTime,
        searchedFor,

    };
}

function Row(props) {
    const { row } = props.name;
    const [open, setOpen] = React.useState(false);

    let arr = row
    console.log(arr.length)
    let projects = []
    let projectNames = []

    const Gesucht = 'Project A'


    arr.forEach(element => {
        if (projects.includes(element.projectName)) {
            console.log('schon drin')
        } else {
            projects.push(element.projectName)
        }
    });

    projects.forEach(element => {
        if (element == Gesucht) {
            console.log('hier')


        } else {
            console.log('nicht hier')
            console.log(element)
        }
    })

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
                            </Table>
                        </Box>
                    </Collapse>
                </TableCell>
            </TableRow>
        </React.Fragment>
    );
}



const rows = [
    createData('Project A', 'Use Case erstellen A', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project A', 'Use Case erstellen A1', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project B', 'Use Case erstellen B', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project C', 'Use Case erstellen C', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project D', 'Use Case erstellen D', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project E', 'Use Case erstellen E', '2020-01-02', 'Max Musterfrau', 14, 5),
];

const rowNames = []
const rowActivities = []


rows.forEach(element => {
    rowNames.push(element.name)
})

rows.forEach(element => {
    rowActivities.push(element.activities)
})

console.log(rowNames)

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
                <div>


                    {rows.map(element => (
                        <TableBody>
                            <TableRow key={element} row={element}>{element.name}</TableRow>
                            <TableCell >{element.activities}</TableCell>
                            <TableCell >{element.employee}</TableCell>
                            <TableCell >{element.planedTime}</TableCell>
                            <TableCell >{element.bookedTime}</TableCell>
                        </TableBody>
                    ))}
                </div>

            </Table>
        </TableContainer >
    );
}
/*row.projects.map((projectsRow) => (
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
)*/