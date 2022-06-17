import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';

function Row(props) {
    const { row } = props;
    const [open, setOpen] = React.useState(false);

    function columns() {
        const columns = [
            {
                id: 'activity',
                label: 'Activity',
                minWidth: 170
            },
            {
                id: 'capacity',
                label: 'Capacity in (h)',
                minWidth: 100
            },
            {
                id: 'current_capacity',
                label: 'Booked Time in (h)',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toLocaleString('de-DE'),
            },
            {
                id: 'employee',
                label: 'Employee',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toLocaleString('en-US'),
            },
            {
                id: 'delta',
                label: 'Delta (h)',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toFixed(2),
            },
        ];
        return columns
    }

    function createData(activity, capacity, current_capacity) {
        const delta = capacity - current_capacity;
        return { activity, capacity, current_capacity, delta };
    }

    function smth() {
        let newthingy = []
        const activities = ['A', 'A', 'B', 'C', 'D']
        const planedTimes = [1, 4, 2, 3]
        const bookedTimes = [1, 1, 1]
        const employees = []

        for (var i = 0; i <= activities.length; i++) {
            let new_data = createData(activities[i], planedTimes[i], bookedTimes[i])
            newthingy.push(new_data)
        }
        return newthingy
    }

    const liste = [1]
    return (
        <React.Fragment>
            <TableRow sx={{ '& > *': { borderBottom: 'unset' } }}>
                {liste.map((column) => {
                    const value = row.activity;
                    return (
                        <TableCell align={column.align}>
                            <IconButton
                                aria-label="expand row"
                                size="small"
                                onClick={() => setOpen(!open)}
                            > Für Infos zur Aktivität: {value}, bitte klicken
                                {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                            </IconButton>
                        </TableCell>
                    );
                })}
                <TableCell hover>

                </TableCell>
            </TableRow>
            <TableRow>
                <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                    <Collapse in={open} timeout="auto" unmountOnExit>
                        <Box sx={{ margin: 0.5 }}>
                            <Table size="small" aria-label="purchases">
                                <TableHead>
                                    <TableRow>
                                        {columns().map((column) => (
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
                                    <TableRow hover  >
                                        {columns().map((column) => {
                                            const value = row[column.id];
                                            return (
                                                <TableCell align={column.align}
                                                    key={row[column.id]}>
                                                    {value}
                                                </TableCell>
                                            );
                                        })}
                                    </TableRow>
                                </TableBody>
                            </Table>
                        </Box>
                    </Collapse>
                </TableCell>
            </TableRow>
        </React.Fragment>
    );
}



function createData(activity, capacity, current_capacity) {
    const delta = capacity - current_capacity;
    return { activity, capacity, current_capacity, delta };
}

function rows() {
    let newthingy = []
    const activities = ['A', 'B', 'A', 'C']
    const planedTimes = [1, 2, 3, 4]
    const bookedTimes = [1, 1, 1, 2]
    const employees = []

    for (var i = 0; i < activities.length; i++) {
        let new_data = createData(activities[i], planedTimes[i], bookedTimes[i])
        newthingy.push(new_data)
    }

    let liste = {}
    newthingy.forEach((element, index) => {
        for (var elem in liste) {
            if (elem == element) {
                liste[element] = elem.current_capacity + element.value
            }
            console.log('Hier dict: ', elem)
            liste[element.activity] = element.current_capacity
        }


    }, console.log(liste),

    )
    return newthingy

}

function toFindDuplicates(arry) { arry.filter((item, index) => arry.indexOf(item) !== index) }
const duplicateElementa = toFindDuplicates(rows());
console.log('Hier sind die Duplikate: ', duplicateElementa)

export default function CollapsibleTable(props) {
    return (

        <Table aria-label="collapsible table">
            <TableBody>
                {rows().map((row) => (
                    <Row row={row} />
                ))}
            </TableBody>
        </Table>

    );
}
