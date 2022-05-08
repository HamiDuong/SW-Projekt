/*import React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import './ProjectWorkTime.css';

//Fake Data for column-filling:
const columns = [
    { id: 'date', label: 'Date', minWidth: 100 },
    { id: 'sollstunden', label: 'Sollstunden', minWidth: 100 },
    {
        id: 'iststunden',
        label: 'Iststunden',
        minWidth: 100,
        align: 'right',
        //format: (value) => value.toLocaleString('en-US'),
    },
    {
        id: 'delta',
        label: 'Delta',
        minWidth: 100,
        align: 'right',
        format: (value) => value.toFixed(2),
    },
];


function createData(date, iststunden, sollstunden) {
    const delta = sollstunden - iststunden;
    return { date, iststunden, sollstunden, delta };
}

function totalTime(times) {
    return times.map(({ delta }) => delta).reduce((sum, i) => sum + i, 0);
}


const rows = [
    createData('21.08.2022', 7, 9),
    createData('12.03.2022', 8, 9),
    createData('08.08.2022', 10, 9),
    createData('21.08.2022', 7, 9),
    createData('12.03.2022', 8, 9),
    createData('08.08.2022', 10, 9),
];

const timetotalTime = totalTime(rows);

class ProjectWorkTime extends React.Component {
    constructor(props) {
        super(props);
    }
    state = {}
    render() {
        return (
            <Paper sx={{ width: '90%', overflow: 'hidden', margin: 'auto' }}>
                <TableContainer sx={{ maxHeight: 440 }} size='small' classprojectname="Tablecontainer">
                    <Table stickyHeader aria-label="sticky table">
                        <TableHead>
                            <TableRow>
                                {columns.map((column) => (
                                    <TableCell
                                        key={column.id}
                                        align={column.align}
                                        style={{ minWidth: column.minWidth }}
                                    >
                                        {column.label}
                                    </TableCell>
                                ))}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows
                                .map((row) => {
                                    return (
                                        <TableRow hover role="checkbox" tabIndex={-1} key={row.date}>
                                            {columns.map((column) => {
                                                const value = row[column.id];
                                                return (
                                                    <TableCell key={column.id} align={column.align}>
                                                        {column.format && typeof value === 'number'
                                                            ? column.format(value)
                                                            : value}
                                                    </TableCell>
                                                );
                                            })}
                                        </TableRow>
                                    );

                                })}
                            <TableRow>
                                <TableCell rowSpan={3} />
                                <TableCell colSpan={2} classprojectname="totalTime">Total time</TableCell>
                                <TableCell align="right" >{timetotalTime}</TableCell>
                            </TableRow>
                        </TableBody>
                    </Table>
                </TableContainer>
            </Paper>
        );
    }
}

export default ProjectWorkTime; */

/*import * as React from 'react';
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

function createData(projectname, sollzeiten, istzeiten, delta, date, activity, employee) {
    return {
        projectname,
        sollzeiten,
        istzeiten,
        activity,
        delta,
    };
}



function Row(props) {
    const { row } = props;
    const [open, setOpen] = React.useState(false);
}

function Cell(props) {
    const { cell } = props;
    const [open, setOpen] = React.useState(false);

}

const cells = [
    createData('Activity A', 7, 9),
    createData('Activity B', 8, 9),
    createData('Activity C', 10, 9)
];

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
            <TableCell component="th" scope="row">
                {row.projectname}
            </TableCell>
            <TableCell align="right">{row.sollzeiten}</TableCell>
            <TableCell align="right">{row.istzeiten}</TableCell>
            <TableCell align="right">{row.delta}</TableCell>
        </TableRow>
        <TableRow>
            <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                <Collapse in={open} timeout="auto" unmountOnExit>
                    <Box sx={{ margin: 1 }}>
                        <Typography variant="h6" gutterBottom component="div">
                            Detailed View
                        </Typography>
                        <Table size="small" aria-label="purchases">
                            <TableHead>
                                <TableRow>
                                    <TableCell>{cells.map((cell) => (
                                        <Cell key={cell.projectname} cell={cell} />))}
                                    </TableCell>
                                    <TableCell>Employee</TableCell>
                                    <TableCell>Date</TableCell>
                                    <TableCell >Booked Time</TableCell>
                                </TableRow>
                            </TableHead>
                        </Table>
                    </Box>
                </Collapse>
            </TableCell>
        </TableRow>
    </React.Fragment>
);




const rows = [
    createData('Project A', 7, 9),
    createData('Project B', 8, 9),
    createData('Project C', 10, 9),
    createData('Project D', 7, 9),
    createData('Project E', 8, 9),
    createData('Project F', 10, 9),
];

export default function CollapsibleTable() {
    return (
        <TableContainer component={Paper}>
            <Table aria-label="collapsible table">
                <TableHead>
                    <TableRow>
                        <TableCell />
                        <TableCell>Project</TableCell>
                        <TableCell align="right">Sollstunden&nbsp;(h)</TableCell>
                        <TableCell align="right">Booked time&nbsp;(h)</TableCell>
                        <TableCell align="right">Delta&nbsp;(h)</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {rows.map((row) => (
                        <Row key={row.projectname} row={row} />
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}*/