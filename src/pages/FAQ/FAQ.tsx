import Typography from '@mui/material/Typography';

import Meta from '@/components/Meta';
import { FullSizeCenteredFlexBox } from '@/components/styled';
import Paper from '@mui/material/Paper/Paper';
import { Button } from '@mui/material';
import { Link } from 'react-router-dom';


const FAQ = () => {
  return (
    <>
    <Meta title="FAQ" />
    <div style={{ padding: '20px' }}>
    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
      <Typography variant="h4">
        Frequently Asked Questions
      </Typography>
      <Button component={Link} to="/qolscripts" variant="contained" color="primary">
        Go to QOL Scripts
      </Button>
    </div>
      <Paper style={{ padding: '20px', marginTop: '20px' }}>
        <Typography variant="h6" gutterBottom>
          Script Instructions
        </Typography>

        <Typography variant="subtitle1" gutterBottom>
          What is a JSON Blob?
        </Typography>
        <Typography paragraph>
          A JSON Blob is a stringified JSON object that contains the data you want to process. It should be properly formatted and valid JSON.
        </Typography>

        <Typography variant="subtitle1" gutterBottom>
          Running a Postman Request
        </Typography>
        <Typography paragraph>
          For some scripts, you'll need to run a Postman request first to obtain the necessary data. Follow the API documentation to construct your request.
        </Typography>
      </Paper>
    </div>
    </>
  );
};

export default FAQ;
