import { styled } from '@mui/system';

const tableStyle = styled('table')({
  width: '85%',
  borderSpacing: '0',
  borderCollapse: 'collapse',
  '& th': {
    textAlign: 'left',
    padding: '0.5rem',
    borderBottom: '1px solid #ddd',
  },
  '& td': {
    padding: '0.5rem',
    borderBottom: '1px solid #ddd',
  },
  '& tr:hover': {
    backgroundColor: '#ddd',
  },
  display: "inline-block",
});

export {tableStyle};
