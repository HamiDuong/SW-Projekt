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
                activity: 'Projektkosten aufbereiten',
                date: '2020-01-02',
                employee: 'Max Musterfrau',
                plannedTime: 14,
                bookedTime: 5,
            },
            {
                projectName: 'Project B',
                activity: 'Projektkosten aufbereiten',
                date: '2020-01-02',
                employee: 'Max Musterfrau',
                plannedTime: 14,
                bookedTime: 5,
            },
        ],
    };
}
function UserGreeting(props) {
    return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
    return <h1>Please sign up.</h1>;
}

function myfuncyy() {
    return
    <UserGreeting />;
}

function Row(props) {
    const { row } = props;
    const [open, setOpen] = React.useState(false);

    let arr = row.projects

    //console.log(arr.length)

    const search_for = 'Project A'
    let result = []

    arr.forEach(elem => {
        if (elem.projectName == search_for) {
            result.push(elem)
            console.log(result)
        }
    });

    const issearchedfor = (row.name == 'Project A')
    console.log('Länge von', arr.length)


    function myfuncy(projectname) {
        let activitiesForProject = []
        for (let i = 0; i <= arr.length; i++) {
            if (arr[i].projectName == projectname) {
                activitiesForProject.push(arr[i].activity)

            } else {
                break
            }
        } return
        (<Button>Hallo</Button>)
    }




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
                    {row.name}
                </TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
                <TableCell align="right"></TableCell>
            </TableRow>
            <div>
                {this.myfuncyy()}
            </div>
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
    createData('Project A', ['Use Case erstellen A', 'XXX'], '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project B', 'Use Case erstellen B', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project C', 'Use Case erstellen C', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project D', 'Use Case erstellen D', '2020-01-02', 'Max Musterfrau', 14, 5),
    createData('Project E', 'Use Case erstellen E', '2020-01-02', 'Max Musterfrau', 14, 5),
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
