from util import *
def solvePI(**kwargs):
    """
    Generalized PI controller function using keyword arguments.

    Parameters:
    - **kwargs: Keyword arguments. Mandatory parameters are T, T_setpoint, Kc, Ki, PIcontrolStepSize, and hc.
    Optional parameters are errorRecord, lowerBounds, and upperBounds.
    Supports non-iterable and iterable arguments.
    
    Returns:
    - A list with PI control results for each input set.
    """
    # Mandatory parameters
    required_params = ['T', 'T_setpoint', 'Kc', 'Ki', 'PIcontrolStepSize', 'hc']
    for param in required_params:
        if param not in kwargs:
            raise ValueError(f"Missing required parameter: {param}")
    # Initialize Mandaratory Parameters
    T, T_setpoint, Kc, Ki, PIcontrolStepSize, hc = [kwargs[param] for param in required_params]

    # Initialize Optional Parameters
    isArray = kwargs.get('isArray', False)
    isEncrypted = kwargs.get('encrypted', False)
    errorRecord = kwargs.get('errorRecord',[[] for _ in T] if isArray else [])
    lowerBounds = kwargs.get('lowerBounds')
    upperBounds = kwargs.get('upperBounds')
    precision = kwargs.get('precision', 12)

    # Quantize the bounds if provided and Encryped, otherwise leave as is or use defaults if not provided.
    lowerBounds = ([-np.inf for _ in T] if isArray else -np.inf) if lowerBounds is None else (decrypt(encrypt(lowerBounds, 'Q', isArray=isArray,d1=precision), 'Q', isArray=isArray) if isEncrypted else lowerBounds)
    upperBounds = ([np.inf for _ in T] if isArray else np.inf)   if upperBounds is None else (decrypt(encrypt(upperBounds, 'Q', isArray=isArray,d1=precision), 'Q', isArray=isArray) if isEncrypted else upperBounds)

    # Dimension Checking
    if isArray:
        requiredParams = [T, T_setpoint, Kc, Ki, lowerBounds, upperBounds, errorRecord]
        if len(set(map(len, requiredParams))) != 1:
            raise ValueError("T, T_setpoint, Kc, Ki, lowerBounds, upperBounds, and errorRecord must have the same length.")

    # To simulate the real process, the input signal is pre-encrypted
    error = T_setpoint - T #if ~isEncrypted else encrypt(T_setpoint, 'Q', isArray=isArray) - encrypt(T, 'Q', isArray=isArray)
    Kc = encode(Kc, 'Q', isArray=isArray,d1=precision)               if isEncrypted else Kc
    Ki = encode(Ki, 'Q', isArray=isArray,d1=precision)               if isEncrypted else Ki
    hc = encode(hc, 'Q', d1=precision)                               if isEncrypted else hc
    PIcontrolStepSize = encode(PIcontrolStepSize, 'Q', d1=precision) if isEncrypted else PIcontrolStepSize

    u = Kc * error + Ki * np.sum(errorRecord, axis=1 if isArray else None) * PIcontrolStepSize * hc
    
    # Write the error to the errorRecord
    for i, err in enumerate(np.atleast_1d(error)):
        errorRecord[i].append(err) if isArray else errorRecord.append(err)

    # We only decrypt at the actuator.
    # In the case of Aspen, this means we need to decrypt prior to writing since there is no way to decrypt in Aspen.
    if isEncrypted:
        u = decrypt(u,'Q',isArray = isArray)
    
    return np.clip(u, lowerBounds, upperBounds) #Clip the final control input to the bounds