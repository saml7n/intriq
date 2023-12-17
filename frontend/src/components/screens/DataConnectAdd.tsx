import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';
import { useNavigation } from '~/lib/NavigationContext';
import { redirect, useNavigate, useRevalidator, useSubmit } from 'react-router-dom';
import { useRef, useState } from 'react';
import Navbar from '../shared/Navbar';
import { motion } from 'framer-motion';
import { DefaultService as api, Document } from '~/lib/client';

interface DataSourceTypeCardProps {
  name: string;
  description: string;
  imgSrc: string;
  selected?: boolean;
  onClickHandler: () => void;
}

const detailsVariants = {
  intial: {
    opacity: 0,
    height: 0,
  },
  open: {
    opacity: 1,
    height: 'auto',
  },
  closed: {
    opacity: 0,
    height: 0,
  },
};

const DataSourceTypeCard: React.FC<DataSourceTypeCardProps> = ({
  name,
  description,
  imgSrc,
  selected,
  onClickHandler,
}) => {
  return (
    <div
      className={`card card-compact w-52 h-60 ${
        selected ? 'bg-base-100 border-secondary' : 'bg-base-200 border-base-200'
      } border hover:bg-base-100 hover:border-secondary shadow-xl cursor-pointer`}
      onClick={onClickHandler}
    >
      <figure>
        <img src={imgSrc} alt="logo" />
      </figure>
      <div className="card-body">
        <h2 className="card-title">{name}</h2>
        <p>{description}</p>
      </div>
    </div>
  );
};

function readFile(file: File){
  return new Promise<string>((resolve, reject) => {
    var fr = new FileReader();  
    fr.addEventListener('load',
    () => { resolve(fr.result as string)});
    fr.addEventListener('error', reject);
    fr.readAsDataURL(file);
  });
}

function DataConnectAdd() {
  const { completedStep, setCompletedStep } = useNavigation();
  const [isSubmitDisabled, setIsSubmitDisabled] = useState<boolean>(true);
  const [selectedDataSourceType, setSelectedDataSourceType] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const navigate = useNavigate();
  const submit = useSubmit();
  function onSubmitClickHandler(event: any): void {
    if (completedStep < 2) setCompletedStep(2);
    const file = fileInputRef.current?.files?.[0];
    if (!file) return
    const document: Document = {
      id: '',
      name:  file.name,
      type: selectedDataSourceType!,
      dataURL: null,
      triplet_id: null,
      embedding_id: null
    }
    readFile(file).then((data) => api.createDocumentDocumentPost({...document, dataURL: data})).then(() => navigate('/connect-data'));
  }

  function onAbortClickHandler(event: any): void {
    navigate('/connect-data');
  }

  return (
    <>
      <Head title="Add a new Data Source" />
      <Navbar title="Add a new Data Source" />
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 z-10">
          <div className="form-control">
            <div className="flex flex-wrap items-center gap-2">
              <DataSourceTypeCard
                name="SAP Connector"
                description="v2 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SAP'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SAP');
                }}
              />
              <DataSourceTypeCard
                name="Sage Connector"
                description="v42 automatic import"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'Sage'}
                onClickHandler={() => {
                  setSelectedDataSourceType('Sage');
                }}
              />
              <DataSourceTypeCard
                name="Operational Data"
                description="file upload: XLSX, XSL, PDF"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'OperationalFile'}
                onClickHandler={() => {
                  setSelectedDataSourceType('OperationalFile');
                }}
              />
              <DataSourceTypeCard
                name="Financial Data"
                description="file upload: XLSX, XSL, PDF"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'FinancialFile'}
                onClickHandler={() => {
                  setSelectedDataSourceType('FinancialFile');
                }}
              />
              <DataSourceTypeCard
                name="Retail Operations"
                description="interview transcript"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'RetailInterview'}
                onClickHandler={() => {
                  setSelectedDataSourceType('RetailInterview');
                }}
              />
              <DataSourceTypeCard
                name="Sales & Marketing"
                description="interview transcript"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SalesMarkingInterview'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SalesMarkingInterview');
                }}
              />
              <DataSourceTypeCard
                name="Supply Chain Management"
                description="interview transcript"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'SupplyChainInterview'}
                onClickHandler={() => {
                  setSelectedDataSourceType('SupplyChainInterview');
                }}
              />
              <DataSourceTypeCard
                name="Human Resources Management"
                description="interview transcript"
                imgSrc="https://daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.jpg"
                selected={selectedDataSourceType === 'HRInterview'}
                onClickHandler={() => {
                  setSelectedDataSourceType('HRInterview');
                }}
              />
            </div>
          </div>
        </section>
        <section className="col-span-12 xl:col-span-6 z-10">
          <hr className="my-6 border-t-2 border-base-content/5" />
          {/* SAP & Sage Integration */}
          <motion.section
            initial={false}
            animate={['SAP', 'Sage'].includes(selectedDataSourceType || '') ? 'open' : 'closed'}
            variants={detailsVariants}
            className="col-span-12 xl:col-span-4 overflow-hidden"
          >
            <div className="form-control">
              <label className="label">
                <span className="label-text">Server URL</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">API token</span>
              </label>
              <input type="text" placeholder="Type here" className="input input-bordered" />
            </div>
          </motion.section>
          {/* Operational & Financial File */}
          <motion.section
            initial={false}
            animate={['OperationalFile', 'FinancialFile'].includes(selectedDataSourceType || '') ? 'open' : 'closed'}
            variants={detailsVariants}
            className="col-span-12 xl:col-span-4 overflow-hidden"
          >
            <label className="form-control w-full max-w-xs">
              <div className="label">
                <span className="label-text">Pick a file</span>
              </div>
              <input ref={fileInputRef} type="file" className="file-input file-input-bordered w-full max-w-xs" />
              <div className="label">
              <span className="label-text-alt"></span>
                <span className="label-text-alt">{selectedDataSourceType}</span>
              </div>
            </label>
          </motion.section>

          {selectedDataSourceType && <hr className="my-6 border-t-2 border-base-content/5" />}
          <div className="form-control">
            <div className="flex items-center gap-2">
              <button className="btn btn-outline btn-error w-1/3" onClick={onAbortClickHandler}>
                Abort
              </button>
              <button
                className={`btn ${selectedDataSourceType ? 'btn-primary' : 'btn-disabled'} w-2/3`}
                onClick={onSubmitClickHandler}
              >
                Add new Data Source
              </button>
            </div>
          </div>
        </section>
      </div>
    </>
  );
}

export default DataConnectAdd;
