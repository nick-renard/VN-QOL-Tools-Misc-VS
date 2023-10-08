import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Button, Chip } from '@mui/material';
import Meta from '@/components/Meta';
import ScriptDrawer from '@/sections/ScriptDrawer/ScriptDrawer';
import { Link } from 'react-router-dom';
import { scriptRows } from '../../config/index'

import { useState } from 'react';
interface ScriptData {
  id: number;
  scriptName: string;
}

const QOLScripts = () => {
  const [isDrawerOpen, setDrawerOpen] = useState(false);
  const [selectedScript, setSelectedScript] = useState<null | ScriptData>(null);

  const executeScript = (scriptId: number, inputData: Record<string, any>) => {
    console.log(`Executing script with ID ${scriptId} and input data`, inputData);
    // Here, you could call an API to execute the script on the backend,
    // or execute some client-side code based on the selected script.
  };

  const columns: GridColDef[] = [
    { field: 'id', headerName: 'ID', flex: 0.1 },
    { field: 'scriptName', headerName: 'Script Name', flex: .3 },
    { field: 'description', headerName: 'Description', flex: 1 },
    {
      field: 'action',
      headerName: 'Action',
      flex: 0.2,
      renderCell: (params) => {
        const scriptData: ScriptData = params.row as ScriptData;
        return (
          <Button
            variant="contained"
            color="primary"
            onClick={() => {
              setDrawerOpen(true);
              setSelectedScript(scriptData);
            }}
          >
            Open Script Drawer
          </Button>
        );
      },
    },
  ];

  return (
    <>
    <Meta title='QOL Scripts' />
    <div style={{ height: 'auto', marginLeft: '50px', marginRight: '50px', marginTop: '36px', whiteSpace: 'pre' }}>
    <div style={{ marginBottom: '20px' }}>
        <Button component={Link} to="/faq" variant="contained" color="primary">
          Have questions? Go to FAQs
        </Button>
      </div>
        <DataGrid
          rows={scriptRows}
          columns={columns}
          initialState={{
            pagination: {
              paginationModel: { page: 0, pageSize: 10 },
            },
          }}
          pageSizeOptions={[10, 25]}
          disableColumnMenu />
        <ScriptDrawer
          isOpen={isDrawerOpen}
          onClose={() => setDrawerOpen(false)}
          scriptData={selectedScript}
          executeScript={executeScript}
        />
      </div>
    </>
  );
};

export default QOLScripts;
