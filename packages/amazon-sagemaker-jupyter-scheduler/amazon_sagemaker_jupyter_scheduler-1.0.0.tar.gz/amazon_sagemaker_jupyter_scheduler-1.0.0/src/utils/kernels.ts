import isString from 'lodash/isString';
import { KERNELSPEC_NAME_SEPARATOR } from '../constants';
import { ParsedSpecName } from '../types';

function parseSageMakerKernelSpecName(name: string | undefined): ParsedSpecName {
  // Parse a kernelspec into different parts
  // Example kernelspec: kernelname__SAGEMAKER_INTERNAL__arn:aws:sagemaker:region:account:image/imagename/version
  // Parsed result: { kernel: kernelname, arnEnvironment: arn:aws:sagemaker:region:account:image/imagename, version: version }
  try {
    if (!isString(name) || name.length === 0) {
      return { kernel: null, arnEnvironment: null, version: null };
    }

    const splitName = name.split(KERNELSPEC_NAME_SEPARATOR);
    const [kernel, environment] = splitName;
    const splitEnv = environment && environment.split('/');

    const arnEnvironment = splitEnv && splitEnv[0] + '/' + splitEnv[1];
    const version = splitEnv.length === 3 ? splitEnv[2] : null;

    return { kernel, arnEnvironment, version };
  } catch (e) {
    return { kernel: null, arnEnvironment: null, version: null };
  }
}

export { parseSageMakerKernelSpecName };
