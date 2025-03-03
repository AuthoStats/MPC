from constants import *
def wipeFolder(folder, delete_all=False):
    """
    Wipes the specified folder by either removing specified files or the entire folder.

    : param folder    : Path to the folder to be wiped.
    : param delete_all: Boolean flag to determine if the whole folder should be deleted.
                       If False, only specified files will be deleted.
    """
    # Ensure the folder path is absolute
    folder = os.path.abspath(folder)

    if delete_all:
        try:
            # Remove the folder and all its contents
            shutil.rmtree(folder)
            print(f"Deleted entire folder: {folder}")
        except PermissionError:
            print(f"Permission denied: Could not delete the folder {folder}")
        except FileNotFoundError:
            print(f"Folder not found: {folder}")
        except Exception as e:
            print(f"Unexpected error deleting folder {folder}: {e}")
        print("Wipe process completed.")
    else:
        # List of files to check and delete if they exist
        files_to_delete = [
            'greenLightAspen',
            'greenLightPython',
            'u.txt',
            'dynamicValues.txt'
        ]
        for file_name in files_to_delete:
            file_path = os.path.join(folder, file_name)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except PermissionError:
                    print(f"Permission denied: Could not delete {file_path}")
                except FileNotFoundError:
                    print(f"File not found: {file_path}")
                except Exception as e:
                    print(f"Unexpected error deleting {file_path}: {e}")
            else:
                print(f"File does not exist: {file_path}")
        print("File deletion process completed.")
################################################################################################################################


def timeFunction(function, *params, runs=100, per_run=100, **kwargs):
    #params = (input1, input2, input3)
    #kwargs = {'key1': value1, 'key2': value2}
    
    # Use timeit.repeat to get multiple measurements
    stmt = lambda: function(*params,**kwargs)
    timings = timeit.repeat(stmt=stmt, repeat=runs, number=per_run)

    # Convert timings into numpy array for easier statistical analysis
    timings = np.array(timings) / per_run  # Convert to time per execution

    # Calculate statistics
    mean = np.mean(timings)
    std_dev = np.std(timings)
    max_time = np.max(timings)
    min_time = np.min(timings)
    percentile_1 = np.percentile(timings, 1)   # 1% Low
    percentile_5 = np.percentile(timings, 5)   # 5% Low
    percentile_95 = np.percentile(timings, 95)  # 5% High
    percentile_99 = np.percentile(timings, 99)  # 1% High

    # Print statistics
    print(f"Mean execution time: {mean:.3e} seconds")
    print(f"Standard Deviation: {std_dev:.3e}")
    print(f"1% Low: {percentile_1:.3e} seconds")
    print(f"5% Low: {percentile_5:.3e} seconds")
    print(f"1% High: {percentile_99:.3e} seconds")
    print(f"5% High: {percentile_95:.3e} seconds")
    print(f"Min execution time: {min_time:.3e} seconds")
    print(f"Max execution time: {max_time:.3e} seconds")


################################################################################################################################
public_key_Q, private_key_Q = paillier.generate_paillier_keypair(n_length=256)
def encrypt(val, state, d1=12,isArray = False):
    match state:
        # case 'Q':
        #     result = np.empty_like(np.atleast_1d(val))
        #     for i,x in enumerate(val):
        #         result[i]=public_key_Q.encrypt(x,precision=2**(-d1))
        #     return np.squeeze(result)
        case 'Q': return np.vectorize(lambda x: public_key_Q.encrypt(x,precision=2**(-d1)))(val) if isArray else  public_key_Q.encrypt(val, precision=2**(-d1))
        case _: raise ValueError("Invalid State Variable")
def encode(val, state, d1=12,isArray = False):
    match state:
        case 'Q': return np.vectorize(lambda x: paillier.EncodedNumber.encode(public_key_Q,x,precision=2**(-d1)))(val) if isArray else  paillier.EncodedNumber.encode(public_key_Q,val,precision=2**(-d1))
        case _: raise ValueError("Invalid State Variable")

def decrypt(val, state,isArray = False):
    match state:
        case 'Q': return np.vectorize(lambda x: private_key_Q.decrypt(x))(val) if isArray else  private_key_Q.decrypt(val)
        case _: raise ValueError("Invalid State Variable")