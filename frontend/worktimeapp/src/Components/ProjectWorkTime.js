import React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';

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

function createData(date, sollstunden, iststunden) {
    const delta = sollstunden - iststunden;
    return { date, sollstunden, iststunden, delta };
}

const rows = [
    createData('Get-from-Backend', 7, 9),
    createData('Get-from-Backend', 8, 9),
    createData('Get-from-Backend', 10, 9),
    createData('Get-from-Backend', 7, 9),
    createData('Get-from-Backend', 5, 9),
    createData('Get-from-Backend', 6, 9),
    createData('Get-from-Backend', 7, 9),
];


class ProjectWorkTime extends React.Component {
    constructor(props) {
        super(props);
    }
    state = {}
    render() {
        return (
            <Paper sx={{ width: '90%', overflow: 'hidden', margin: 'auto' }}>
                <TableContainer sx={{ maxHeight: 440 }} size='small'>
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
                        </TableBody>
                    </Table>
                </TableContainer>
            </Paper>
        );
    }
}

export default ProjectWorkTime;
