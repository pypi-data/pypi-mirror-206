import React, { useMemo, useEffect } from 'react';
import { Scheduler } from '@jupyterlab/scheduler';

import { SelectInputContainer } from '../SelectInputContainer';
import { ImagesMap } from '../../../types';

import { ImageSelectorOption } from './ImageSelectorOption';
import { Kernel, FormState } from '../CreateNotebookJobform';

// const ImageTooltipLink = 'https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-images.html';
// const KernelTooltipLink = 'https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-kernels.html';

import * as styles from './styles';
import Alert from '@mui/material/Alert';
import { getImageOptionsFromMap } from '../../../utils';
import { i18nStrings } from '../../../constants';
import { DropdownItem } from '../../../components/selectinput';

interface Props {
  isDisabled: boolean;
  imagesMap: ImagesMap;
  selectedKernel: Kernel;
  formState: FormState;
  formErrors: Scheduler.ErrorsType;
  setFormState: React.Dispatch<React.SetStateAction<FormState>>;
  setFormErrors: (errors: Scheduler.ErrorsType) => void;
  setSelectedKernel: (selectedKernel: Kernel) => void;
}

const JobEnvironment: React.FunctionComponent<Props> = ({
  isDisabled,
  imagesMap,
  selectedKernel,
  formState,
  formErrors,
  setFormState,
  setFormErrors,
  setSelectedKernel,
}) => {
  const imageDropdownItems = getImageOptionsFromMap(imagesMap);

  const kernelDropdownItems = useMemo(() => {
    if (selectedKernel.arnEnvironment && imagesMap[selectedKernel.arnEnvironment]) {
      const kernelOptions = imagesMap[selectedKernel.arnEnvironment].kernelOptions;
      return kernelOptions.map((kernelOption) => ({ label: kernelOption.displayName, value: kernelOption.name }));
    }
    return [];
  }, [imagesMap, selectedKernel]);

  const handleImageSelection = (item: DropdownItem | string) => {
    if (typeof item === 'string') {
      return;
    }
    const selectedImageArn = item.value;
    const kernelItems = imagesMap[selectedImageArn].kernelOptions || [];
    const kernel: string | null = kernelItems.length > 0 ? kernelItems[0].name : null;

    setFormState({
      ...formState,
      sm_image: selectedImageArn,
      sm_kernel: kernel ?? '',
    });
    setSelectedKernel({ arnEnvironment: selectedImageArn, kernel });
  };

  const handleKernelSelection = (item: DropdownItem | string) => {
    if (typeof item !== 'string') {
      const selectedKernelValue = item.value;
      setFormState({ ...formState, sm_kernel: selectedKernelValue });
      setSelectedKernel({ ...selectedKernel, kernel: selectedKernelValue });
    }
  };

  const isError = !!formErrors.jobEnvironmentError;
  const errorMessageWithIcon = (
    <div className={styles.ErrorIconStyled}>
      <Alert severity="error">{formErrors.jobEnvironmentError}</Alert>
    </div>
  );

  useEffect(() => {
    if (selectedKernel.arnEnvironment && selectedKernel.kernel) {
      if (formErrors.jobEnvironmentError) {
        setFormErrors({
          ...formErrors,
          jobEnvironmentError: '',
        });
      }
    }
  }, [selectedKernel.arnEnvironment, selectedKernel.kernel]);

  if (Object.keys(imagesMap).length === 0) {
    return null;
  }

  return (
    <div className={styles.JobEnvironmentContainer}>
      <div className={styles.KernelImageSelectorContainer}>
        <div>
          <SelectInputContainer
            id={''}
            label={i18nStrings.ImageSelector.label}
            options={imageDropdownItems}
            value={selectedKernel.arnEnvironment || ''}
            customListItemRender={ImageSelectorOption}
            onChange={handleImageSelection}
            disabled={isDisabled}
          />
          {formErrors.jobEnvironmentError && (
            <div className={styles.ValidationMessageStyled}>{isError && errorMessageWithIcon}</div>
          )}
        </div>
        <SelectInputContainer
          id={''}
          label={i18nStrings.KernelSelector.label}
          options={kernelDropdownItems}
          value={selectedKernel.kernel || ''}
          onChange={handleKernelSelection}
          disabled={isDisabled}
        />
      </div>
    </div>
  );
};

export { JobEnvironment };
